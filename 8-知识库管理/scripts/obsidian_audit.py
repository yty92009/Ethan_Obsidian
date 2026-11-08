#!/usr/bin/env python3
"""Read-only Obsidian vault scanner and processing-queue generator.

This script never modifies files under the vault. Reports are written only to an
output directory outside the vault.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_EXCLUDED_DIRS = {".obsidian", ".git", ".trash", "node_modules", "venv", ".venv", "dist", "build"}
SOURCE_NOISE_EXTS = {".py", ".js", ".ts", ".tsx", ".jsx", ".java", ".c", ".cpp", ".h", ".cs", ".go", ".rs", ".sh", ".ps1", ".sql", ".html", ".css", ".json", ".xml", ".yaml", ".yml"}
MEDIA_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".mp4", ".mov", ".avi", ".mkv", ".mp3", ".wav", ".zip", ".7z", ".rar", ".woff", ".woff2", ".ttf", ".otf", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"}
TEXT_EXTS = {".md", ".txt", ".csv", ".log"}
TAG_RE = re.compile(r"(?<![\w/])#([\w\-\u4e00-\u9fff][\w\-\u4e00-\u9fff/]*)")
TITLE_RE = re.compile(r"^\s*#\s+(.+?)\s*$")


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def yaml_frontmatter(text: str) -> tuple[dict[str, Any], str | None]:
    if text.startswith("\ufeff"):
        text = text[1:]
    if not text.startswith("---"):
        return {}, None
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, None
    end = next((i for i in range(1, min(len(lines), 501)) if lines[i].strip() in {"---", "..."}), None)
    if end is None:
        return {}, "frontmatter opening marker found without closing marker"
    raw = "\n".join(lines[1:end])
    try:
        import yaml  # type: ignore
        parsed = yaml.safe_load(raw)
        return (parsed if isinstance(parsed, dict) else {}), None
    except ImportError:
        data: dict[str, Any] = {}
        for line in raw.splitlines():
            if ":" in line and not line.startswith((" ", "-")):
                key, value = line.split(":", 1)
                value = value.strip().strip("'\"")
                data[key.strip()] = value
        return data, None
    except Exception as exc:
        return {}, f"frontmatter parse error: {exc}"


def frontmatter_tags(frontmatter: dict[str, Any]) -> list[str]:
    value = frontmatter.get("tags", [])
    if isinstance(value, str):
        value = [value]
    if not isinstance(value, list):
        return []
    return [str(x).lstrip("#").strip() for x in value if str(x).strip()]


def extract_tags(text: str) -> list[str]:
    parts = re.split(r"(```[\s\S]*?```|~~~[\s\S]*?~~~)", text)
    body = "".join(part for i, part in enumerate(parts) if i % 2 == 0)
    body = re.sub(r"https?://\S+", "", body)
    return list(dict.fromkeys(m.group(1) for m in TAG_RE.finditer(body)))


def first_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        match = TITLE_RE.match(line)
        if match:
            return match.group(1).strip().strip("#").strip()
    return fallback


def read_text(path: Path, preferred: str = "auto") -> tuple[str | None, str | None, str | None]:
    encodings = ["utf-8-sig", "utf-8", "gb18030"] if preferred == "auto" else [preferred]
    last_error = None
    for encoding in encodings:
        try:
            return path.read_text(encoding=encoding), encoding, None
        except (UnicodeDecodeError, OSError) as exc:
            last_error = str(exc)
    return None, None, last_error


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def classify(path: Path, rel: str, title: str, tags: list[str], chars: int) -> tuple[str, str, str]:
    low = rel.lower()
    if "/99-收件箱/" in f"/{low}/" or low.startswith("99-收件箱/"):
        return "high", "review_inbox", "已位于收件箱，优先确认处理状态"
    if not title or chars < 120:
        return "high", "triage", "缺少标题或内容较短，需要快速判断是否值得保留"
    topic_text = (rel + " " + title + " " + " ".join(tags)).lower()
    keywords = ("p&l", "powerbi", "数据治理", "跨境电商", "amazon", "agent", "rag", "langchain", "langgraph", "面试", "财务", "利润")
    if any(k in topic_text for k in keywords):
        return "high", "summarize_and_link", "与当前职业主线或 AI 学习主线相关，建议优先总结并关联已有笔记"
    if path.suffix.lower() == ".md":
        return "medium", "summarize", "Markdown 资料，建议生成知识卡片后再决定是否深入阅读"
    return "low", "archive_or_extract", "非 Markdown 文件，当前只完成盘点，后续按需提取"


def scan(args: argparse.Namespace) -> int:
    vault = Path(args.vault).resolve()
    out_root = Path(args.out).resolve()
    if not vault.is_dir():
        print(f"ERROR: vault does not exist or is not a directory: {vault}", file=sys.stderr)
        return 2
    if out_root == vault or vault in out_root.parents:
        print("ERROR: output directory must be outside the vault", file=sys.stderr)
        return 2
    out_root.mkdir(parents=True, exist_ok=True)
    run_dir = out_root / datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir.mkdir(parents=True, exist_ok=False)
    excluded = DEFAULT_EXCLUDED_DIRS | {x.strip() for x in args.exclude_dir}
    items: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    counts: dict[str, int] = {}
    for base, dirs, files in os.walk(vault, topdown=True, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in excluded and not (Path(base) / d).is_symlink())
        for name in sorted(files):
            path = Path(base) / name
            if path.is_symlink():
                continue
            rel = path.relative_to(vault).as_posix()
            ext = path.suffix.lower()
            try:
                stat = path.stat()
                size = stat.st_size
                mtime = datetime.fromtimestamp(stat.st_mtime).astimezone().isoformat(timespec="seconds")
            except OSError as exc:
                errors.append({"path": rel, "error": str(exc)})
                continue
            counts[ext or "[no extension]"] = counts.get(ext or "[no extension]", 0) + 1
            item: dict[str, Any] = {"path": rel, "name": name, "extension": ext, "size": size, "mtime": mtime, "read_status": "counted"}
            if args.hash:
                try:
                    item["sha256"] = sha256(path)
                except OSError as exc:
                    item["warnings"] = [f"hash failed: {exc}"]
            if ext in TEXT_EXTS and size <= args.max_file_mb * 1024 * 1024:
                text, encoding, error = read_text(path, args.encoding)
                item["encoding"] = encoding
                if error or text is None:
                    item["read_status"] = "error"
                    item["warnings"] = [error or "unknown read error"]
                    errors.append({"path": rel, "error": error or "unknown read error"})
                else:
                    fm, fm_error = yaml_frontmatter(text) if ext == ".md" else ({}, None)
                    title = first_title(text, path.stem) if ext == ".md" else path.stem
                    tags = list(dict.fromkeys(frontmatter_tags(fm) + extract_tags(text))) if ext == ".md" else []
                    chars = len(text)
                    item.update({"read_status": "parsed", "frontmatter": fm, "title": title, "tags": tags, "parse_error": fm_error, "stats": {"char_count": chars, "word_count_estimate": len(re.findall(r"\b\w+\b", text)), "line_count": len(text.splitlines())}})
                    if ext == ".md":
                        priority, action, reason = classify(path, rel, title, tags, chars)
                        item["queue"] = {"priority": priority, "action": action, "reason": reason}
            elif ext in SOURCE_NOISE_EXTS or ext in MEDIA_EXTS:
                item["warnings"] = ["counted only; not parsed in conservative profile"]
            items.append(item)
    summary = {"files": len(items), "parsed_text": sum(1 for x in items if x.get("read_status") == "parsed"), "read_errors": len(errors), "by_extension": dict(sorted(counts.items()))}
    report = {"schema_version": "1.0", "generated_at": now_iso(), "vault_root": str(vault), "filters": {"excluded_dirs": sorted(excluded), "max_file_mb": args.max_file_mb, "profile": "conservative", "hash": args.hash}, "summary": summary, "items": items, "errors": errors}
    (run_dir / "scan_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    md_lines = ["# Obsidian 知识库扫描报告", "", f"生成时间：{report['generated_at']}", f"知识库：`{vault}`", "", "## 摘要", "", f"- 文件总数：{summary['files']}", f"- 已解析文本：{summary['parsed_text']}", f"- 读取错误：{summary['read_errors']}", "", "## 扩展名统计", "", "| 扩展名 | 数量 |", "|---|---:|"]
    md_lines += [f"| `{k}` | {v} |" for k, v in summary["by_extension"].items()]
    md_lines += ["", "## Markdown 资料预览", "", "| 优先级 | 路径 | 标题 | 标签 | 建议 |", "|---|---|---|---|---|"]
    for item in items:
        if item.get("extension") == ".md" and item.get("queue"):
            q = item["queue"]
            md_lines.append(f"| {q['priority']} | `{item['path']}` | {item.get('title','')} | {', '.join(item.get('tags', [])) or '-'} | {q['action']} |")
    (run_dir / "scan_report.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    queue = []
    for item in items:
        if item.get("extension") == ".md" and item.get("queue"):
            q = item["queue"]
            queue.append({"queue_id": "q-" + hashlib.sha1(item["path"].encode()).hexdigest()[:12], "path": item["path"], "title": item.get("title", ""), "priority": q["priority"], "action": q["action"], "reason": q["reason"], "suggested_destination": "02-知识卡片" if q["action"] in {"summarize", "summarize_and_link"} else "99-待确认", "status": "pending", "needs_review": True})
    queue.sort(key=lambda x: {"high": 0, "medium": 1, "low": 2}.get(x["priority"], 9))
    (run_dir / "processing_queue.json").write_text(json.dumps({"schema_version": "1.0", "generated_at": now_iso(), "items": queue}, ensure_ascii=False, indent=2), encoding="utf-8")
    qmd = ["# 资料处理队列", "", "> 仅为建议，不会自动移动、删除或修改原笔记。", "", "| 优先级 | 路径 | 建议动作 | 推荐去向 | 状态 |", "|---|---|---|---|---|"]
    qmd += [f"| {x['priority']} | `{x['path']}` | {x['action']} | {x['suggested_destination']} | {x['status']} |" for x in queue]
    (run_dir / "processing_queue.md").write_text("\n".join(qmd) + "\n", encoding="utf-8")
    print(json.dumps({"run_dir": str(run_dir), "summary": summary, "queue_items": len(queue)}, ensure_ascii=False, indent=2))
    return 1 if args.fail_on_read_error and errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only Obsidian vault audit")
    sub = parser.add_subparsers(dest="command", required=True)
    scan_parser = sub.add_parser("scan")
    scan_parser.add_argument("--vault", required=True)
    scan_parser.add_argument("--out", required=True)
    scan_parser.add_argument("--exclude-dir", action="append", default=[])
    scan_parser.add_argument("--max-file-mb", type=int, default=10)
    scan_parser.add_argument("--hash", action="store_true")
    scan_parser.add_argument("--encoding", default="auto")
    scan_parser.add_argument("--fail-on-read-error", action="store_true")
    scan_parser.set_defaults(func=scan)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
