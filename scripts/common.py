"""各節點共用的小工具：讀 frontmatter、抽數字、切投影片、簡易 Markdown 轉 HTML。"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
WIKI = ROOT / "wiki"
DISCUSS = ROOT / "discussions"
OUTLINE = ROOT / "slides" / "outline.md"

# 小於等於這個值的整數不檢查（2 個量子位元、第 3 步這類數字太常見，比對沒有意義）
SMALL_NUMBER = 10


# ---------- frontmatter ----------
def split_frontmatter(text):
    """回傳 (meta dict, body)。只支援 key: value 與 key: [a, b] 兩種寫法。"""
    meta = {}
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                if ":" not in line:
                    continue
                k, v = line.split(":", 1)
                v = v.strip()
                if v.startswith("[") and v.endswith("]"):
                    v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
                meta[k.strip()] = v
            return meta, text[end + 4:].lstrip("\n")
    return meta, text


def wiki_pages():
    """所有 wiki 內容頁（index.md、log.md 除外），回傳 {slug: (meta, body)}。"""
    pages = {}
    for p in sorted(WIKI.glob("*.md")):
        if p.stem in ("index", "log"):
            continue
        pages[p.stem] = split_frontmatter(p.read_text(encoding="utf-8"))
    return pages


def raw_ids():
    return sorted(p.stem for p in RAW.glob("*.md"))


# ---------- 數字比對 ----------
# 數字後面可以接中文的「萬」「億」，比對時換算成實際數值
NUM_RE = re.compile(r"(?<![\w.])(\d[\d,]*(?:\.\d+)?)\s*(萬|億)?")
LINK_TARGET_RE = re.compile(r"\]\([^)]*\)")
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
# |00⟩、|11\rangle、\lvert 10\rangle 這類 ket 標籤是狀態名稱，裡面的數字不是事實
KET_RE = re.compile(r"(?:\||\\lvert|\\vert)\s*[\w+\-]+\s*(?:⟩|\\rangle)")
UNIT = {"萬": 10_000, "億": 100_000_000}


def numbers_in(text):
    """抽出文字中所有大於 SMALL_NUMBER 的數字，回傳像 "2048"、"300萬" 的字串集合。
    連結網址、HTML 註解、ket 標籤裡的數字不算。"""
    text = KET_RE.sub("", COMMENT_RE.sub("", LINK_TARGET_RE.sub("]()", text)))
    found = set()
    for m in NUM_RE.finditer(text):
        tok = m.group(1).rstrip(",").replace(",", "")
        unit = m.group(2) or ""
        try:
            value = float(tok) * UNIT.get(unit, 1)
        except ValueError:
            continue
        if value <= SMALL_NUMBER:
            continue
        found.add(tok + unit)
    return found


def normalize_for_search(text):
    """把 2,048 變成 2048，讓比對不受千分位影響。"""
    return re.sub(r"(?<=\d),(?=\d{3})", "", text)


def _fmt(x):
    return f"{x:g}"


def find_number(haystack, token):
    """token 是 numbers_in 的輸出。帶「萬」「億」的數字，原文寫成同樣的中文、完整數字、
    或 million / billion 都算找到。"""
    unit = token[-1] if token[-1] in UNIT else ""
    num = token[:-1] if unit else token
    patterns = [rf"(?<![\d.]){re.escape(num)}(?![\d])" if not unit else rf"(?<![\d.]){re.escape(num)}\s*{unit}"]
    if unit:
        # 越具體的寫法越先比對：million / billion，最後才是完整數字（完整數字最容易巧合撞到）
        value = float(num) * UNIT[unit]
        if value >= 1e9:
            patterns.append(rf"(?<![\d.]){re.escape(_fmt(value / 1e9))}\s*billion")
        if value >= 1e6:
            patterns.append(rf"(?<![\d.]){re.escape(_fmt(value / 1e6))}\s*million")
        patterns.append(rf"(?<![\d.]){int(value)}(?![\d])")
    for p in patterns:
        m = re.search(p, haystack)
        if m:
            return m
    return None


def contains_number(haystack, token):
    return find_number(haystack, token) is not None


# ---------- 投影片大綱 ----------
SOURCES_RE = re.compile(r"<!--\s*sources:\s*(.*?)\s*-->")
LAYOUT_RE = re.compile(r"<!--\s*layout:\s*(\w+)\s*-->")


def parse_outline(text=None):
    """大綱以單獨一行的 --- 分隔投影片。回傳 list of dict(title, sources, layout, body)。"""
    if text is None:
        text = OUTLINE.read_text(encoding="utf-8")
    slides = []
    for chunk in re.split(r"^---\s*$", text, flags=re.M):
        chunk = chunk.strip()
        if not chunk:
            continue
        m = SOURCES_RE.search(chunk)
        sources = [s.strip() for s in m.group(1).split(",") if s.strip()] if m else []
        lm = LAYOUT_RE.search(chunk)
        title_m = re.search(r"^#{1,2} (.+)$", chunk, re.M)
        slides.append({
            "title": title_m.group(1).strip() if title_m else "",
            "sources": sources,
            "layout": lm.group(1) if lm else "content",
            "body": chunk,
        })
    return slides


# ---------- 簡易 Markdown 轉 HTML（投影片用） ----------
MATH_RE = re.compile(r"\$\$.+?\$\$|\$[^$\n]+?\$", re.S)


def inline(text):
    maths = []

    def keep(m):
        maths.append(m.group())
        return f"\x00{len(maths) - 1}\x00"

    text = MATH_RE.sub(keep, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    return re.sub(r"\x00(\d+)\x00", lambda m: html.escape(maths[int(m.group(1))], quote=False), text)


def md_to_html(md):
    """支援：# / ## / ### 標題、- 與 1. 清單、> 引言、$$ 區塊數學、以 < 開頭的 HTML 原樣保留、段落。"""
    out, para, lst, lst_tag = [], [], [], None
    lines = COMMENT_RE.sub("", md).splitlines()

    def flush():
        nonlocal para, lst, lst_tag
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para = []
        if lst:
            out.append(f"<{lst_tag}>" + "".join(f"<li>{inline(x)}</li>" for x in lst) + f"</{lst_tag}>")
            lst, lst_tag = [], None

    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if not s:
            flush()
        elif s.startswith("$$"):
            flush()
            block = [s]
            while not (block[-1].endswith("$$") and len("".join(block)) > 2) and i + 1 < len(lines):
                i += 1
                block.append(lines[i].strip())
            out.append('<div class="math">' + html.escape(" ".join(block), quote=False) + "</div>")
        elif s.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            i -= 1
            head = "".join(f"<th>{inline(c)}</th>" for c in rows[0])
            body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
            out.append(f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>")
        elif s.startswith("<"):
            flush()
            out.append(lines[i])
        elif m := re.match(r"^(#{1,3}) (.+)$", s):
            flush()
            n = len(m.group(1))
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
        elif m := re.match(r"^- (.+)$", s):
            if para or lst_tag == "ol":
                flush()
            lst_tag = "ul"
            lst.append(m.group(1))
        elif m := re.match(r"^\d+\. (.+)$", s):
            if para or lst_tag == "ul":
                flush()
            lst_tag = "ol"
            lst.append(m.group(1))
        elif s.startswith("> "):
            flush()
            out.append("<blockquote>" + inline(s[2:]) + "</blockquote>")
        else:
            if lst:
                flush()
            para.append(s)
        i += 1
    flush()
    return "\n".join(out)
