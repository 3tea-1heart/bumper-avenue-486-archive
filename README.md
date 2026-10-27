# 碰碰车大道 486 号 · 聊天档案

这里保存碰碰车大道的完整聊天导出，以及沿用原始设计的网页查看器。

- **77,036 条消息**，39 个数据分片。
- 时间范围：**2025 年 12 月 9 日至 2026 年 10 月 26 日**（北京时间）。
- 完整保留导出目录中的图片、消息和引用索引。原始文件合计约 **1.04 GB**。
- 前端沿用 **QQ Chat Exporter 6.2.6** 原有布局、侧栏、气泡、配色、搜索、筛选、图片查看及深浅色模式。

## 打开档案

在 GitHub 点击 **Code → Download ZIP**，完整解压后打开 `index.html`。请不要只下载 HTML 文件。

也可在 Windows 双击 `Start-Archive.cmd`；它需要 Python 3，会在本机启动服务器并打开浏览器。关闭终端即停止服务。跨平台可运行 `python scripts/serve.py`。

如果需要完全未修改的导出查看器，打开 `original.html`。它使用原始 `assets/app.js`；原始聊天数据由两个入口共用。

## 本次优化

- 默认启用原查看器自带的“记住滚动位置”，可以在设置中关闭。
- 将本档案的主题、阅读位置、设置存储键单独命名，避免与同一地址下其他 QCE 档案相互覆盖。
- `Ctrl+K` / `⌘K` 聚焦原有搜索框。
- 将原先远程加载的 Inter 字体随仓库保存，减少离线时的外部依赖；字体许可见 `assets/Inter-LICENSE.txt`。
- 增加减少动画偏好的支持、加载失败提示、页面元信息和本地启动脚本。
- 原始 `assets/app.js`、`assets/style.css`、`data/` 和 `resources/` 均保留；优化脚本为独立的 `assets/app.optimized.js`。
- 不启用相邻分片预加载，避免默认额外读取大量聊天数据；需要时可在原有设置中开启。

## 完整性检查

运行 `python scripts/verify_archive.py`。该脚本验证 `SOURCE_SHA256.txt` 中每个原始文件的 SHA-256、全部消息数量、分片数量和消息 ID 唯一性。

校验清单中的 `original.html` 对应原导出的 `index.html`。新增优化文件不冒充原始导出。

本仓库保存的是所提供导出的完整文件，不能恢复导出时就已缺失的附件、撤回消息或不可访问的外部链接。远程 QQ 头像等仍可能需要联网；离线时原查看器使用已有的回退行为。

## 仓库与访问

仓库用于私有备份。上传 GitHub 仓库不等于部署了可直接访问的网页，HTML 在 GitHub 文件页中显示为源码。当前不启用 GitHub Pages；下载后可本地阅读。

聊天记录、昵称、账号标识和图片按原始导出保留，没有做匿名化处理。请在决定分享档案前确认分享范围。

## 来源与权利

原始导出工具：[shuakami/qq-chat-exporter](https://github.com/shuakami/qq-chat-exporter)，原查看器使用 [shuakami/hyperscroll](https://github.com/shuakami/hyperscroll)。本仓库保留原查看器内的来源链接。

聊天内容与附件的权利属于各自权利人。本仓库未对聊天内容、原导出工具或第三方素材作出新的开放许可声明。
