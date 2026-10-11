# GitHub 与 ChatGPT 发布操作指南

核实日期：2026-10-11。

## 1. 先明确你发布的是什么

本包连接已经运行的 `https://tanmai.net/mcp`。GitHub 发布的是插件配置和下载文件，服务仍由探脉提供。GitHub Pages 只能托管静态内容，不能承载这个有 OAuth 和业务查询的 MCP 服务。若想把探脉服务端本身开源，还需要服务端源代码、部署配置和开源授权，本包不包含这些内容。

公开 GitHub 仓库与 Release 不需要 OpenAI 的公司/个人主体认证。提交 ChatGPT 官方插件目录需要独立办理身份、域名验证和审核；GitHub 仓库链接不是审核替代品。

## 2. 网页创建仓库

1. 登录 GitHub，打开 https://github.com/new 。
2. Owner 选自己的账号或你有权限的组织。
3. Repository name 建议 `tanmai-mcp-plugin`。
4. Description 可填：`探脉 Tanmai：通过 OAuth 接入只读经营数据 MCP。`
5. Visibility 选 Public，让他人可以访问和下载。
6. 使用本包 README 时，不勾选初始化 README；许可证尚未确定时先不选 License。
7. 点击 Create repository。

你的仓库地址会是 `https://github.com/你的用户名/tanmai-mcp-plugin`。这里的“你的用户名”必须换成实际账号；当前没有替你创建仓库。

## 3. 上传解压后的文件

1. 下载 ZIP 并解压，得到 `tanmai` 文件夹。
2. 打开文件夹，确认看到 `plugin.json`、`mcp.json`、`README.md`、`assets`、`docs`、`package.py`。
3. 仓库页面选择 Add file → Upload files。新建空仓库也可使用页面上的 uploading an existing file 链接。
4. 把 `tanmai` **里面的内容**上传到仓库根目录。最终根目录应直接出现 `plugin.json`；不要多套一层 `tanmai/`。
5. 提交信息填 `Initial Tanmai MCP plugin v0.1.0`，点击 Commit changes。
6. 查看根目录和 assets/docs，确认文件均已提交。

不要只把 ZIP 上传进代码目录。源码应解压提交；ZIP 放在 Release 附件，便于安装和下载。

## 4. 发布第一个 Release

1. 仓库右侧 Releases → Create a new release；也可打开仓库地址后加 `/releases/new`。
2. Choose a tag → 输入 `v0.1.0` → 创建新标签，Target 选 `main` 或仓库实际默认分支。
3. Release title 填 `Tanmai MCP Plugin v0.1.0`。
4. 说明可填写：

   首次发布探脉远程 MCP 插件连接包。连接 https://tanmai.net/mcp，使用 OAuth 授权，仅查询当前账号授权范围内的经营数据。每位用户需独立授权。包不含服务端源码或任何账号凭据。官方目录审核尚未完成。

5. 上传本次 ZIP `tanmai-0.1.0.zip` 作为附件。
6. 点击 Publish release。

可分享的地址：

- 仓库：`https://github.com/你的用户名/tanmai-mcp-plugin`
- 当前版本：`https://github.com/你的用户名/tanmai-mcp-plugin/releases/tag/v0.1.0`
- 最新版本：`https://github.com/你的用户名/tanmai-mcp-plugin/releases/latest`
- 固定版本 ZIP：`https://github.com/你的用户名/tanmai-mcp-plugin/releases/download/v0.1.0/tanmai-0.1.0.zip`

优先使用你上传的 ZIP。GitHub 自动生成的 Source code ZIP 会带仓库名称前缀和全部仓库文件，其结构可能不同于插件安装器要求。

## 5. 终端方式（与网页方式二选一）

先安装 Git、完成 GitHub 登录/SSH 或凭据配置。进入解压后的 tanmai 目录，执行：

```bash
git init -b main
git add .
git commit -m "Initial Tanmai MCP plugin v0.1.0"
git remote add origin https://github.com/YOUR_USERNAME/tanmai-mcp-plugin.git
git push -u origin main
git tag v0.1.0
git push origin v0.1.0
```

先把 `YOUR_USERNAME` 替换为实际用户名。不要把账号密码或访问令牌写入 remote URL。已有 Git 仓库不要重复 init 或添加同名 origin；已有网页初始提交时先 clone 再复制本包文件。

安装并登录 GitHub CLI 后，可以发布 Release：

```bash
gh auth login
gh release create v0.1.0 ../tanmai-0.1.0.zip --title "Tanmai MCP Plugin v0.1.0" --notes "Initial release: read-only remote MCP connection with OAuth."
```

## 6. 后续更新

修改源码后，把 `plugin.json` 的版本改为 `0.1.1`，运行 `python3 package.py`，得到目录外的 `tanmai-0.1.1.zip`。提交更改，创建 `v0.1.1` 标签，再创建新 Release 并上传新 ZIP。包版本、标签和附件文件名应一致。

仓库创建后，可把真实 repository URL 写入 `plugin.json` 的 `repository` 字段。不要写占位 URL。选择许可证后，再添加 LICENSE 及合法的 license 字段。

## 7. 先测试真实授权

在 ChatGPT 网页端按 README 添加 MCP，完成 OAuth，再查询测试商户的数据。确认身份/权限范围、金额、时间口径、店铺榜和撤销授权后的处理。准备录屏用的样例数据，避免暴露真实经营数据。安装 ZIP 并不等于 OAuth 已授权。

## 8. 如果还要发布到 ChatGPT 官方目录

先补齐准备材料：

1. 确定经验证的个人或公司发布身份，以及目标国家/地区和是否存在付费购买。不要根据域名推断这些信息。
2. 准备四个真实公开 HTTPS 页面：官网、支持联系页面、隐私政策、服务条款。首页已核实；其余三项本次未找到。政策须反映实际收集、使用、共享、留存和删除数据的做法。
3. 准备专用测试账号、样例商户与测试数据。账号要能独立登录并覆盖案例；凭据只填审核后台安全字段，不写入 ZIP/GitHub。
4. 按 REVIEW.md 跑完 5 个正向、3 个反向案例，校准真实工具和参数，记录结果；录制实际操作视频并提供审核可访问的链接。脚本不能替代真实录像。
5. 将核实后的身份、URL、商业声明、国家和演示链接写入插件元数据，再重新打包。当前未知值没有虚构填写。

材料完成后：

1. 打开 OpenAI Developer Dashboard： https://platform.openai.com/ ，选择发布组织与项目，进入 Plugins。具体页面入口以当前后台为准。
2. 完成个人/企业身份验证；非组织 owner 需要 Apps Management Write 权限。
3. 选择 Upload new or existing plugin，选发布者身份，再上传 ZIP。这一步建立草稿。
4. 在 Metadata & Skills 检查元数据扫描结果，修复问题并上传新版本。
5. 在 MCPs 选择 tanmai → Connect，确认 URL、OAuth 以及 DCR 配置。
6. 完成后台给出的域名挑战。在其要求的 HTTPS 域名 `/.well-known/openai-apps-challenge` 路径返回精确的纯文本挑战值。需要有探脉域名/服务器配置权限；GitHub 仓库地址不能替代 tanmai.net 的控制权验证。
7. 完成 OAuth，等待工具扫描，检查每个工具的 readOnlyHint/openWorldHint/destructiveHint 是否为符合实际行为的布尔值。有问题需改探脉服务端，本仓库连接配置不能替服务端补注解。
8. 填 Review details，核对导入案例、视频、发行说明、国家、商业声明；安全字段填写测试账号。用该版本重新验证案例。
9. 由你完成政策声明，再点击 Submit for review。等待审核反馈并修复问题。
10. 获批后，打开批准版本点击 Publish plugin。提交审核与发布上线是两个动作。

## 官方参考

- 探脉接入：https://tanmai.net/docs/mcp.md
- GitHub 创建仓库：https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
- GitHub 上传文件：https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- GitHub Release：https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository
- OpenAI 插件格式：https://developers.openai.com/plugins/build/plugins
- OpenAI 提交与发布：https://developers.openai.com/plugins/deploy/submission
- OpenAI MCP 审核要求：https://developers.openai.com/plugins/deploy/app-review
