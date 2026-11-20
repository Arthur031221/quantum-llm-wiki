// 共用的 Markdown 顯示工具：讀 frontmatter、保護數學式、用 marked 轉 HTML、改寫連結。
const REPO = "https://github.com/Arthur031221/quantum-llm-wiki/blob/main/";

function splitFrontmatter(text) {
  const meta = {};
  if (!text.startsWith("---\n")) return { meta, body: text };
  const end = text.indexOf("\n---", 4);
  text.slice(4, end).split("\n").forEach((line) => {
    const i = line.indexOf(":");
    if (i < 0) return;
    let v = line.slice(i + 1).trim();
    if (v.startsWith("[") && v.endsWith("]")) v = v.slice(1, -1).split(",").map((s) => s.trim()).filter(Boolean);
    meta[line.slice(0, i).trim()] = v;
  });
  return { meta, body: text.slice(end + 4).replace(/^\n+/, "") };
}

// marked 會吃掉反斜線，先把 $...$ 換成佔位符，轉完再放回去
function renderMarkdown(md) {
  const maths = [];
  const kept = md.replace(/\$\$[\s\S]+?\$\$|\$[^$\n]+?\$/g, (m) => `@@MATH${maths.push(m) - 1}@@`);
  const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  return marked.parse(kept).replace(/@@MATH(\d+)@@/g, (_, i) => esc(maths[+i]));
}

// basePath：這份 Markdown 在 repo 裡所在的資料夾，例如 "wiki/" 或 ""
function fixLinks(root, basePath) {
  root.querySelectorAll("a[href]").forEach((a) => {
    const href = a.getAttribute("href");
    if (/^(https?:|#|mailto:)/.test(href) || href.endsWith(".html") || href.includes(".html#")) return;
    if (!href.endsWith(".md")) return;
    const full = new URL(href, "https://x/" + basePath).pathname.slice(1);
    const m = full.match(/^wiki\/([\w-]+)\.md$/);
    if (m) a.setAttribute("href", `wiki.html#${m[1]}`);
    else { a.setAttribute("href", REPO + full); a.setAttribute("target", "_blank"); }
  });
}

function renderMath(root) {
  if (window.renderMathInElement) {
    renderMathInElement(root, { delimiters: [
      { left: "$$", right: "$$", display: true }, { left: "$", right: "$", display: false }] });
  } else {
    setTimeout(() => renderMath(root), 100);
  }
}
