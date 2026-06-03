#!/usr/bin/env python3
"""Generate docs/*.md, samples/*.csv, samples/sjis/*.csv from spec/*.json (SSOT).

Usage:
  python3 tools/build.py            # write outputs
  python3 tools/build.py --check    # build into memory and diff vs working tree (CI)
"""
import json, os, sys, glob, io, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC_DIR = os.path.join(ROOT, "spec")

MARKERS = ("(必須)", "（必須）")

def clean_name(name):
    for m in MARKERS:
        name = name.replace(m, "")
    return name.strip()

def render_md(spec):
    title = spec["title"]
    m = spec["meta"]
    src = spec["source"]
    kubun = "取込（インポート）" if spec["direction"] == "import" else "出力（エクスポート）"
    header = "あり" if m.get("header") else "なし"
    out = []
    out.append(f"## {title}")
    out.append("")
    out.append(f"> ⚠️ **非公式資料です。** {src['note']}  ")
    out.append(f"> 公式マニュアル: <{src['manual']}>")
    out.append("")
    out.append("### CSV仕様")
    out.append("")
    out.append("| 項目 | 内容 |")
    out.append("|------|------|")
    out.append(f"| 区分 | {kubun} |")
    out.append(f"| 文字コード | {m['encoding']} |")
    out.append(f"| 区切り文字 | `{m['delimiter']}`（カンマ） |")
    out.append(f"| 囲み文字 | {m['quote']} |")
    out.append(f"| 改行コード | {m['newline']} |")
    out.append(f"| ヘッダ行 | {header} |")
    out.append("")
    out.append(f"### 項目一覧（全{len(spec['fields'])}項目）")
    out.append("")
    out.append("| # | 項目名 | 桁数 | 属性 | 必須 | 項目説明 |")
    out.append("|---|--------|------|------|:----:|----------|")
    for i, f in enumerate(spec["fields"], 1):
        req = "○" if f.get("required") else ""
        out.append(f"| {i} | {clean_name(f['name'])} | {f['length']} | {f['type']} | {req} | {f['desc']} |")
    out.append("")
    out.append(f"> このファイルは [`spec/{title}.json`](../spec/{title}.json) から自動生成しています。"
               "修正は `spec` を編集し `python3 tools/build.py` を実行してください。")
    out.append("")
    return unicodedata.normalize("NFC", "\n".join(out))

def csv_header(spec):
    return unicodedata.normalize("NFC", ",".join(clean_name(f["name"]) for f in spec["fields"])) + "\r\n"

def outputs():
    """Yield (relpath, bytes) for every generated file."""
    for path in sorted(glob.glob(os.path.join(SPEC_DIR, "*.json"))):
        spec = json.load(open(path, encoding="utf-8"))
        title = spec["title"]
        yield f"docs/{title}.md", render_md(spec).encode("utf-8")
        header = csv_header(spec)
        yield f"samples/{title}.csv", header.encode("utf-8")
        try:
            yield f"samples/sjis/{title}.csv", header.encode("cp932")
        except UnicodeEncodeError as e:
            print(f"WARN cp932 encode failed for {title}: {e}", file=sys.stderr)
            yield f"samples/sjis/{title}.csv", header.encode("cp932", errors="replace")


def island_rows():
    """Parse docs/離島地域.md table, forward-filling blank 都道府県/市区郡."""
    rows = []
    pref = city = ""
    started = False
    for line in open(os.path.join(ROOT, "docs/離島地域.md"), encoding="utf-8"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 3:
            continue
        body = "".join(cells)
        if set("".join(line.split("|")[1:-1])) <= set("-: "):
            started = True            # separator row -> data starts next
            continue
        if not started:               # header row
            continue
        pref = cells[0] or pref
        city = cells[1] or city
        area = cells[2]
        if not area:
            continue
        rows.append({"都道府県": pref, "市区郡": city, "住所": area})
    return rows

def island_outputs():
    rows = island_rows()
    # CSV (UTF-8, header + data)
    lines = ["都道府県,市区郡,住所"]
    for r in rows:
        vals = [f'"{r[k]}"' if ("," in r[k]) else r[k] for k in ("都道府県","市区郡","住所")]
        lines.append(",".join(vals))
    csv = unicodedata.normalize("NFC", "\r\n".join(lines) + "\r\n")
    yield "data/離島地域.csv", csv.encode("utf-8")
    js = json.dumps(rows, ensure_ascii=False, indent=2)
    yield "data/離島地域.json", (unicodedata.normalize("NFC", js) + "\n").encode("utf-8")

def main():
    check = "--check" in sys.argv
    diffs = []
    gen = list(outputs()) + list(island_outputs())
    for rel, data in gen:
        full = os.path.join(ROOT, rel)
        if check:
            cur = open(full, "rb").read() if os.path.exists(full) else None
            if cur != data:
                diffs.append(rel)
        else:
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "wb") as f:
                f.write(data)
            print(f"wrote {rel}")
    if check:
        if diffs:
            print("OUT OF SYNC (run tools/build.py):")
            for d in diffs:
                print("  -", d)
            sys.exit(1)
        print("all generated files in sync ✓")

if __name__ == "__main__":
    main()
