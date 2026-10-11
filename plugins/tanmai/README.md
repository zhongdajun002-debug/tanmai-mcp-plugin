# 探脉 Tanmai MCP 插件

通过远程 MCP 与 OAuth 授权，查询探脉中用户有权访问的电商经营数据。

## 接入参数

| 项目 | 值 |
| --- | --- |
| MCP 地址 | `https://tanmai.net/mcp` |
| 传输 | Streamable HTTP |
| 认证 | OAuth 2.1 + PKCE，动态客户端注册 |
| 权限 | `mcp:read`，只读 |
| 官方说明 | https://tanmai.net/docs/mcp.md |

此仓库提供插件连接配置，不包含探脉服务端源码，不部署新的服务器。安装后，每位用户仍需登录探脉并授权。GitHub 仓库公开不代表经营数据公开。

## 文件

- `plugin.json`：Agent Plugins 1.0 插件元数据。
- `mcp.json`：远程 MCP 与 OAuth 配置；无账号密码、令牌或 Client Secret。
- `assets/icon.png`：由探脉官网 SVG 图标转换的 512 × 512 PNG。
- `docs/PUBLISH.md`：GitHub 上传、Release、终端操作及 ChatGPT 目录发布说明。
- `docs/REVIEW.md`：后续提交官方目录时可使用的测试草稿与录屏步骤。
- `docs/VERIFICATION.md`：实际完成的验证及尚未验证的内容。
- 市场仓库根目录的 `package.py`：重新打包脚本。

## 使用

支持 Agent Plugins 的客户端：按客户端提供的插件 ZIP / 仓库安装入口安装，启用并完成 OAuth。不同客户端的 ZIP、仓库导入支持不同；一个 GitHub 地址并非所有客户端通用的安装入口。

ChatGPT：在支持的网页设置中启用开发者模式，添加自定义 MCP 服务器，URL 填 `https://tanmai.net/mcp`，认证选 OAuth，Client ID / Secret 留空，然后登录探脉并授权。GitHub 上的包不会自动加入 ChatGPT 官方目录。

Codex CLI：

```bash
codex mcp add tanmai --url https://tanmai.net/mcp
```

未自动弹出授权时：

```bash
codex mcp login tanmai
```

Claude Code：

```bash
claude mcp add --transport http tanmai https://tanmai.net/mcp
```

进入 Claude Code 后使用 `/mcp`，选择 tanmai → Authenticate。

授权后可以问：“查询本月销售额和净销售额”“比较本周与上周销售表现”“按店铺排出销售额前十名”。实际可用指标及工具以授权后服务端返回为准。

## 发布状态

当前为 `0.1.0` GitHub 分发包。连接地址及 OAuth 发现信息已经核实；未完成账号授权、实时工具枚举或经营查询实测。官方目录所需发布者身份、支持/隐私/条款页面、目标国家、商业声明、演示视频和测试账号尚待补充，不称为提交就绪包。

没有指定开源许可证。若希望他人可依法复制、修改和再分发，请由仓库所有者选择许可证并确认官网品牌图标的使用授权；仓库可见性与开源授权是不同事项。
