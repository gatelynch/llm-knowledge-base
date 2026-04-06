#!/usr/bin/env python3
"""
Facebook JSON 匯出 → Obsidian Markdown 轉換腳本

讀取 Facebook 下載的貼文 JSON，轉換為 Obsidian 格式的 Markdown 檔案。
只處理有文字內容的貼文，媒體檔案複製到輸出目錄的 assets/ 子目錄。

用法：
  python3 scripts/facebook_to_md.py <facebook匯出資料夾> [輸出目錄]

  輸出目錄預設為 raw/notes/social/facebook/
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from collections import defaultdict


def fix_encoding(text: str) -> str:
    """修正 Facebook JSON 的 latin1-encoded UTF-8 問題"""
    try:
        return text.encode("latin1").decode("utf-8")
    except (UnicodeDecodeError, UnicodeEncodeError):
        return text


def sanitize_filename(text: str, max_len: int = 20) -> str:
    """從貼文文字取前 N 字作為檔名摘要"""
    clean = re.sub(r"\s+", " ", text).strip()
    clean = clean[:max_len]
    clean = re.sub(r'[\\/:*?"<>|]', "", clean)
    clean = clean.strip(". ")
    return clean or "無標題"


def extract_post_text(post: dict) -> str | None:
    """從貼文的 data 欄位提取文字內容"""
    for d in post.get("data", []):
        if "post" in d:
            return fix_encoding(d["post"])
    return None


def extract_links(post: dict) -> list[str]:
    """提取貼文中的外部連結"""
    links = []
    for att in post.get("attachments", []):
        for ad in att.get("data", []):
            if "external_context" in ad:
                url = ad["external_context"].get("url", "")
                if url:
                    links.append(url)
    return links


def extract_media(post: dict) -> list[dict]:
    """提取貼文附帶的媒體資訊"""
    media_list = []
    for att in post.get("attachments", []):
        for ad in att.get("data", []):
            if "media" in ad:
                uri = ad["media"].get("uri", "")
                if uri:
                    media_list.append({"uri": uri})
    return media_list


def copy_media_file(uri: str, fb_export: Path, assets_dir: Path) -> str | None:
    """複製媒體檔案到 assets/，回傳檔名"""
    src = fb_export / uri
    if not src.exists():
        return None
    filename = src.name
    dst = assets_dir / filename
    if dst.exists() and dst.stat().st_size != src.stat().st_size:
        stem = dst.stem
        suffix = dst.suffix
        counter = 1
        while dst.exists():
            dst = assets_dir / f"{stem}_{counter}{suffix}"
            counter += 1
        filename = dst.name
    if not dst.exists():
        shutil.copy2(src, dst)
    return filename


def generate_md(post_text: str, date_str: str, timestamp: int,
                links: list[str], media_filenames: list[str]) -> str:
    """生成 Obsidian Markdown 內容"""
    lines = [
        "---",
        "origin: self",
        "source: facebook",
        f"date: {date_str}",
        f"timestamp: {timestamp}",
        "tags: [facebook]",
        "---",
        "",
        post_text,
    ]

    if links:
        lines.append("")
        lines.append("## 連結")
        for link in links:
            lines.append(f"- {link}")

    if media_filenames:
        lines.append("")
        lines.append("## 附件")
        for fname in media_filenames:
            lines.append(f"![[assets/{fname}]]")
            lines.append("")

    return "\n".join(lines) + "\n"


def find_posts_json(fb_export: Path) -> Path | None:
    """在 Facebook 匯出資料夾中找到貼文 JSON 檔"""
    candidates = [
        fb_export / "your_facebook_activity/posts/your_posts__check_ins__photos_and_videos_1.json",
        # 有些匯出版本可能用不同檔名
        *sorted(fb_export.glob("**/your_posts*.json")),
    ]
    for p in candidates:
        if p.exists():
            return p
    return None


def convert(fb_export: Path, output_dir: Path):
    """主轉換邏輯"""
    assets_dir = output_dir / "assets"
    output_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(parents=True, exist_ok=True)

    # 找到貼文 JSON
    posts_json = find_posts_json(fb_export)
    if not posts_json:
        print(f"錯誤：在 {fb_export} 找不到貼文 JSON 檔")
        sys.exit(1)

    with open(posts_json, "r") as f:
        posts = json.load(f)

    print(f"讀取到 {len(posts)} 則貼文（來源：{posts_json.name}）")

    # 過濾有文字的貼文
    text_posts = []
    for post in posts:
        text = extract_post_text(post)
        if text:
            text_posts.append((post, text))

    text_posts.sort(key=lambda x: x[0]["timestamp"])
    print(f"有文字內容的貼文：{len(text_posts)} 則")

    date_counter = defaultdict(int)
    created = 0
    media_copied = 0

    for post, text in text_posts:
        ts = post["timestamp"]
        dt = datetime.fromtimestamp(ts)
        date_str = dt.strftime("%Y-%m-%d")
        date_prefix = dt.strftime("%Y%m%d")

        date_counter[date_prefix] += 1
        seq = date_counter[date_prefix]

        summary = sanitize_filename(text)
        filename = f"{date_prefix}-{seq} {summary}.md"

        links = extract_links(post)
        media_items = extract_media(post)

        media_filenames = []
        for m in media_items:
            fname = copy_media_file(m["uri"], fb_export, assets_dir)
            if fname:
                media_filenames.append(fname)
                media_copied += 1

        md_content = generate_md(text, date_str, ts, links, media_filenames)

        out_path = output_dir / filename
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        created += 1

    print(f"\n完成！")
    print(f"  建立 MD 檔：{created} 個")
    print(f"  複製媒體檔：{media_copied} 個")
    print(f"  輸出位置：{output_dir}")
    print(f"  媒體位置：{assets_dir}")


def main():
    if len(sys.argv) < 2:
        print("用法：python3 .claude/scripts/facebook_to_md.py <facebook匯出資料夾> [輸出目錄]")
        sys.exit(1)

    fb_export = Path(sys.argv[1]).resolve()
    if not fb_export.is_dir():
        print(f"錯誤：{fb_export} 不是有效的資料夾")
        sys.exit(1)

    vault_root = Path(__file__).resolve().parent.parent.parent
    output_dir = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else vault_root / "raw/notes/social/facebook"

    convert(fb_export, output_dir)


if __name__ == "__main__":
    main()
