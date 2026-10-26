// Small keyboard and loading improvements; QCE owns the original interface.
'use strict';
document.addEventListener('keydown', event => {
  if (!(event.ctrlKey || event.metaKey) || event.key.toLowerCase() !== 'k') return;
  const input = document.querySelector('input[type="search"][placeholder="搜索消息"]');
  if (!input) return;
  event.preventDefault();
  const sidebar = input.closest('aside');
  if (sidebar && (sidebar.getBoundingClientRect().right <= 1 || getComputedStyle(sidebar).visibility === 'hidden')) {
    document.querySelector('button[aria-label="切换侧栏"]')?.click();
  }
  requestAnimationFrame(() => { input.focus(); input.select(); });
});
window.addEventListener('error', event => {
  if (!(event.target instanceof HTMLScriptElement)) return;
  if (!event.target.src.includes('app.optimized.js')) return;
  const message = document.createElement('p');
  message.className = 'archive-load-error';
  message.append('网页脚本没有加载成功。请完整下载并解压仓库后重试，或打开 ');
  const link = document.createElement('a'); link.href = 'original.html'; link.textContent = '原版查看器';
  message.append(link); document.body.append(message);
}, true);
