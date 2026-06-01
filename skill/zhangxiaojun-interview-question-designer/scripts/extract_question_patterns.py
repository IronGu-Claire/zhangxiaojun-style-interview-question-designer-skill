#!/usr/bin/env python3
"""Extract likely host question patterns from a Chinese interview transcript."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


QUESTION_CUES = [
    "我想问",
    "想问",
    "为什么",
    "怎么理解",
    "你觉得",
    "能不能",
    "是不是",
    "什么样",
    "怎么看",
    "底层",
    "本质",
    "变化",
    "判断",
    "取舍",
    "选择",
]


def clean_line(line: str) -> str:
    line = re.sub(r"^\[[0-9:]+\]\s*", "", line.strip())
    line = re.sub(r"^(张小珺|小珺|主持人)[:：]\s*", "", line)
    return line


def classify(line: str) -> str:
    if any(word in line for word in ["为什么", "怎么理解", "底层", "本质", "机制"]):
        return "机制追问"
    if any(word in line for word in ["变化", "范式", "阶段", "时刻"]):
        return "变化/时间线"
    if any(word in line for word in ["选择", "取舍", "资源", "分配", "成本"]):
        return "决策/取舍"
    if any(word in line for word in ["组织", "团队", "人才", "负责人"]):
        return "组织问题"
    if any(word in line for word in ["未来", "接下来", "信号"]):
        return "未来判断"
    return "通用深挖"


def extract(text: str, limit: int) -> list[tuple[str, str]]:
    candidates: list[tuple[str, str]] = []
    for raw in text.splitlines():
        line = clean_line(raw)
        lowered = line.lower()
        if lowered.startswith("- source:") or "http://" in lowered or "https://" in lowered:
            continue
        if lowered.startswith("- title:") or lowered.startswith("- date:") or lowered.startswith("- duration:"):
            continue
        if len(line) < 8 or len(line) > 180:
            continue
        if "？" in line or "?" in line or any(cue in line for cue in QUESTION_CUES):
            candidates.append((classify(line), line))
    return candidates[:limit]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        required=True,
        action="append",
        help="Transcript Markdown or text. Repeat for multiple files.",
    )
    parser.add_argument("--out", required=True, help="Output Markdown path")
    parser.add_argument("--limit", type=int, default=120)
    args = parser.parse_args()

    candidates: list[tuple[str, str]] = []
    input_names: list[str] = []
    per_file_limit = max(args.limit, 1)
    for raw_input in args.input:
        path = Path(raw_input)
        input_names.append(path.name)
        text = path.read_text(encoding="utf-8")
        candidates.extend(extract(text, per_file_limit))
    candidates = candidates[: args.limit]
    counts = Counter(category for category, _line in candidates)

    lines = [
        f"# 提问模式抽取：{', '.join(input_names)}",
        "",
        "## 类型分布",
        "",
    ]
    for category, count in counts.most_common():
        lines.append(f"- {category}: {count}")

    lines.extend(["", "## 候选问题/追问", ""])
    for index, (category, line) in enumerate(candidates, start=1):
        lines.append(f"{index}. **{category}**：{line}")

    lines.extend(
        [
            "",
            "## 可复用提示",
            "",
            "- 把高频的“为什么/怎么理解/本质/变化”问题改写成 guest-specific 的机制追问。",
            "- 把短句问题扩展成：背景观察 + 矛盾 + 直接提问 + 具体例子。",
            "- 对每个抽象判断补一个“能不能讲一个具体场景”。",
        ]
    )

    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
