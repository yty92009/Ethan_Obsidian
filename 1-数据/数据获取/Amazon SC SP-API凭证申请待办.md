# Amazon SC SP-API 凭证申请待办

创建日期：2026-07-20
状态：待执行
关联项目：PowerBI 利润数据底层 / Amazon SC 接入

## 结论

当前已有 `D:\powerbi项目\外部交接\sc_api_orders.py`，脚本能连到 Amazon SP-API，也能获取 LWA access token。

但当前 refresh token 属于 Amazon Vendor Central。请求 Seller Central 订单报表时，Amazon 返回：

```text
Report type 2409 does not support account ID of type class com.amazon.partner.account.id.VendorGroupId.
```

这说明问题不是脚本，而是凭证类型不对。要拉 Amazon SC 订单，需要 Seller Central 授权的 SP-API refresh token。

## 要申请什么

申请目标：Seller Central 的 Private Seller SP-API app 凭证。

需要拿到以下信息：

- LWA client id
- LWA client secret
- Seller Central refresh token
- Marketplace id，美国站通常是 `ATVPDKIKX0DER`

注意：不要复用 Vendor Central / Vendors app 的 token。SC 订单报表需要 Sellers 侧授权。

## 前提条件

- Seller Central 账号必须是 Professional selling plan。
- 执行授权的账号最好是 Primary User。
- 如果账号没有 Developer Central 权限，需要先让主账号开权限或由主账号操作。
- 如果还没有 SP-API Developer Profile，需要先提交并通过。

## 操作步骤

1. 登录 Seller Central。
2. 进入 `Apps and Services -> Develop Apps`。
3. 如果页面提示注册开发者资料，先提交 SP-API Developer Profile。
4. 在 Developer Central / App Management 中创建 app client。
5. App 类型选择 Private Seller app。
6. API / account type 选择 Sellers，不要选择 Vendors。
7. 配置 LWA 信息，拿到 LWA client id 和 client secret。
8. 申请或勾选需要的角色：
   - 第一阶段拉订单报表：Orders / Reports 相关权限。
   - 后续拉结算费用：Finances 相关权限。
   - 后续拉库存：Inventory / FBA 相关权限。
9. 在 Seller Central 或 Solution Provider Portal 中对该 app 执行 Authorize app。
10. 授权完成后保存 refresh token。
11. 把 SC 的 `refresh token / client id / client secret` 替换到脚本中，或后续改成本地配置文件读取。
12. 先运行 token 验证，再运行 no-wait 报表创建，最后运行完整下载。

## 验证命令

先验证 token：

```powershell
python "D:\powerbi项目\外部交接\sc_api_orders.py" token
```

再验证能否创建 SC 订单报表：

```powershell
python "D:\powerbi项目\外部交接\sc_api_orders.py" orders --date 2026-07-18 --no-wait
```

如果能返回 `reportId`，说明 Seller Central 报表权限基本通了。

最后下载完整报表：

```powershell
python "D:\powerbi项目\外部交接\sc_api_orders.py" orders --date 2026-07-18
```

## 成功标准

- `token` 命令能获取 access token。
- `orders --date ... --no-wait` 能返回 Seller Central reportId。
- 完整下载后生成：
  - `sc_orders_<date>_<date>.csv`
  - `sc_orders_<date>_<date>.metadata.json`
- CSV 每行包含 `channel = Amz SC`。
- metadata 中记录 report type、marketplace、date range、report id、processing status。

## 失败判断

如果仍返回 `VendorGroupId`，说明仍在使用 VC token。

如果返回 `Unauthorized` / `AccessDenied`，说明 app 授权或角色不足。

如果返回 report type 不支持，优先检查：

- app 是否是 Sellers 类型；
- refresh token 是否来自 Seller Central；
- marketplace 是否正确；
- 是否具备 Orders / Reports 权限。

## 数据治理注意事项

- Amazon SC 是 `Amz SC`，不能写入现有 `Amz VC` 利润结果。
- SC seller/order、VC retail/endpos、VC supply/order 是三个不同业务口径。
- 第一版只落本地 CSV/metadata，不直接写 PostgreSQL。
- 入库前必须补 ODS 表、source registry、batch lineage、质量检查和 mapping 验收。

## 官方文档

- Register your application: https://developer-docs.amazon.com/sp-api/docs/registering-your-application
- Self authorization: https://developer-docs.amazon.com/sp-api/docs/self-authorization
- Reports API request flow: https://developer-docs.amazon.com/sp-api/docs/request-a-report
- Order report types: https://developer-docs.amazon.com/sp-api/docs/report-type-values-order

## 待办清单

- [ ] 确认 Seller Central 是 Professional plan。
- [ ] 用 Primary User 登录 Seller Central。
- [ ] 进入 `Apps and Services -> Develop Apps`。
- [ ] 提交或确认 SP-API Developer Profile 已通过。
- [ ] 创建 Private Seller app。
- [ ] 确认 app/API 类型是 Sellers。
- [ ] 保存 LWA client id。
- [ ] 保存 LWA client secret。
- [ ] 授权 app 并生成 Seller Central refresh token。
- [ ] 确认美国站 marketplace id：`ATVPDKIKX0DER`。
- [ ] 替换或配置 `sc_api_orders.py` 的 SC 凭证。
- [ ] 运行 `token` 验证。
- [ ] 运行 `orders --date 2026-07-18 --no-wait` 验证 reportId。
- [ ] 运行完整下载命令生成 CSV 和 metadata。
- [ ] 核对 Seller Central 手工订单报表与脚本输出字段/行数。
- [ ] 再决定是否设计 PostgreSQL ODS 入库表。
