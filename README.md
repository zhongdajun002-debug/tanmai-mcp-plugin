# 探脉插件市场

这是可放到 GitHub 并由支持的 ChatGPT 桌面端 / Codex 添加的插件市场。市场包含连接 `https://tanmai.net/mcp` 的探脉插件；每位用户需要独立完成 OAuth 授权。

## 发布到 GitHub

1. 创建 Public 仓库，建议名 `tanmai-mcp-plugin`。
2. 将本目录的全部内容提交到仓库根目录，包括隐藏的 `.agents` 目录。
3. 确认仓库里能访问 `.agents/plugins/marketplace.json` 和 `plugins/tanmai/plugin.json`。
4. 创建 `v0.1.0` Release，上传 `dist/tanmai-0.1.0.zip` 作为插件附件。

如果浏览器上传忽略了隐藏目录，优先使用 Git 命令或 GitHub Desktop。也可用 GitHub 的 Add file → Create new file，文件名输入 `.agents/plugins/marketplace.json`，粘贴本包同名文件内容并提交。

## 添加市场并安装

如果你的 ChatGPT 桌面端提供“添加市场”且支持 GitHub 来源，在该入口填真实仓库地址，选择“探脉插件市场”，安装并启用“探脉 Tanmai”，完成 OAuth。该 UI 入口是否开放以当前客户端和账号为准，本次没有操作你的界面验证。

官方文档明确支持的 Codex CLI 路径：

```bash
codex plugin marketplace add YOUR_USERNAME/tanmai-mcp-plugin --ref main
codex plugin marketplace list
```

把 `YOUR_USERNAME` 换为真实 GitHub 用户名。然后重新启动 ChatGPT 桌面端，在 Work / Codex 的 Plugins Directory 选择“探脉插件市场”，浏览并安装插件。认证方式是 OAuth，服务器地址为 `https://tanmai.net/mcp`。

更新市场：

```bash
codex plugin marketplace upgrade tanmai-marketplace
```

这是用户主动添加的 GitHub 市场，不会自动出现在官方公共插件目录。官方文档确认支持桌面/本地来源；网页与手机可用性不由这条分发方式保证。

## 终端上传（新建空仓库）

在当前目录执行，先替换 `YOUR_USERNAME`：

```bash
git init -b main
git add .
git commit -m "Initial Tanmai marketplace v0.1.0"
git remote add origin https://github.com/YOUR_USERNAME/tanmai-mcp-plugin.git
git push -u origin main
```

若仓库已有文件，请先 clone，再将本目录内容复制进仓库，提交并 push。

## 重新打包

修改 `plugins/tanmai/plugin.json` 的版本后，在仓库根目录执行：

```bash
python3 package.py
```

打包后的插件 ZIP 写入 `dist/`。提交源码，再创建与版本一致的标签和 Release。下载者不应把整个市场仓库 ZIP 当作单插件 ZIP 安装；单插件包在 dist 中。

## 官方目录是独立流程

GitHub 市场发布无需 OpenAI 主体认证。官方目录发布则需要身份、域名、政策页面、样例测试账号、真实演示录屏、审核及获批后的发布动作。详细说明见 GUIDE.md，其中单插件根目录上传说明仅适用于独立插件仓库；本市场仓库必须使用上方结构。

本包已核实官网接入文档、401 OAuth 挑战和发现元数据。尚未完成授权后的工具枚举与业务查询，不能声称端到端实测通过。没有代你创建 GitHub 仓库、安装插件或发布。

参考：https://developers.openai.com/plugins/build/plugins
