# 验证记录

核实日期：2026-10-11。

- 官网 HTML 明确链接 /docs/mcp.md；已读取接入说明。
- 未认证请求 https://tanmai.net/mcp 返回 HTTP 401，WWW-Authenticate 指向受保护资源元数据。该响应符合受保护接口预期，不是登录成功。
- 受保护资源元数据返回 resource=https://tanmai.net/mcp、authorization_servers=[https://tanmai.net]、scope=mcp:read。
- 授权服务器元数据确认 authorize、token、register 端点，S256、refresh_token、公共客户端及 CIMD 支持。
- 官网连接程序压缩包中的说明列出 list_metrics/get_metric/list_dimensions/query_metrics/compare_periods/rank_by_dimension/whoami；这是文档依据，未从已授权会话枚举实时 schema。
- 当前插件不含本地 skill；取数说明由现有 MCP 服务端提供。
- 已检查打包后 JSON、图标尺寸、路径包含性和市场引用路径。没有运行目标客户端安装或官方后台验证器。
- 未登录、未进行 OAuth 动态注册、未执行经营查询、未检查真实工具 annotations、未测试市场安装。
- 只生成文件，没有创建 GitHub 仓库或提交官方审核。

官方目录缺项：发布者身份、支持 URL、隐私 URL、条款 URL、目标国家/地区、商业声明、实际测试和录屏链接、专用测试账号、域名验证和后台扫描。
