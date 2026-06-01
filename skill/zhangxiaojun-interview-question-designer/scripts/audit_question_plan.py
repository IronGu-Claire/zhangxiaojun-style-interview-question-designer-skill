#!/usr/bin/env python3
"""Audit a Chinese long-form interview question plan."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


GENERIC_PATTERNS = [
    "你怎么看",
    "未来会怎样",
    "介绍一下",
    "有什么困难",
    "有什么建议",
    "最大的挑战是什么",
]

REQUIRED_TERMS = ["采访定位", "嘉宾画像", "时长", "主线", "核心问题", "追问", "必问", "收束"]


def count_questions(text: str) -> int:
    numbered = len(re.findall(r"(?m)^\s*\d+[.、]\s+", text))
    marks = text.count("？") + text.count("?")
    return max(numbered, marks)


def audit(text: str) -> tuple[int, list[str], list[str]]:
    score = 100
    warnings: list[str] = []
    strengths: list[str] = []

    q_count = count_questions(text)
    if q_count < 28:
        score -= 18
        warnings.append(f"问题数量偏少：检测到约 {q_count} 个问题，长访建议至少 28 个。")
    else:
        strengths.append(f"问题数量达到长访准备要求：约 {q_count} 个。")

    missing = [term for term in REQUIRED_TERMS if term not in text]
    if missing:
        score -= 4 * len(missing)
        warnings.append("缺少关键模块：" + "、".join(missing))
    else:
        strengths.append("关键模块完整。")

    if not re.search(r"(120|180|240|360)\s*(分钟|min)", text):
        score -= 10
        warnings.append("没有明确长访时长；建议标出 120/180/240/360 分钟版本。")
    else:
        strengths.append("包含明确长访时长。")

    generic_hits = [pattern for pattern in GENERIC_PATTERNS if pattern in text]
    if generic_hits:
        score -= min(15, 3 * len(generic_hits))
        warnings.append("存在偏泛的问题表达，建议改写：" + "、".join(generic_hits))

    if "具体" not in text and "案例" not in text and "现场" not in text:
        score -= 10
        warnings.append("缺少具体案例/决策现场追问。")
    else:
        strengths.append("包含具体案例或决策现场意识。")

    if "如果" not in text:
        score -= 8
        warnings.append("追问树偏弱：建议加入多个“如果嘉宾这样回答，就这样追”的条件分支。")

    if "质疑" not in text and "风险" not in text and "错" not in text:
        score -= 10
        warnings.append("缺少硬问题：建议加入质疑、风险、判断可能出错的位置。")
    else:
        strengths.append("包含硬问题或风险追问。")

    return max(score, 0), strengths, warnings


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Markdown question plan")
    parser.add_argument("--out", help="Optional audit report path")
    args = parser.parse_args()

    source = Path(args.input)
    text = source.read_text(encoding="utf-8")
    score, strengths, warnings = audit(text)

    report_lines = [
        f"# 采访提纲质量检查：{source.name}",
        "",
        f"综合评分：{score}/100",
        "",
        "## 做得好的地方",
        "",
    ]
    report_lines.extend(f"- {item}" for item in strengths or ["暂无明显强项，建议重做结构。"])
    report_lines.extend(["", "## 需要加强", ""])
    report_lines.extend(f"- {item}" for item in warnings or ["没有发现明显结构问题。"])
    report = "\n".join(report_lines) + "\n"

    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report, encoding="utf-8")
        print(f"Wrote {output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
