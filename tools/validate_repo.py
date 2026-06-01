#!/usr/bin/env python3
"""Validate the public repository layout without external dependencies."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skill" / "zhangxiaojun-interview-question-designer"

REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "README.en.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "CHANGELOG.md",
    "RELEASE_CHECKLIST.md",
    "skill/zhangxiaojun-interview-question-designer/SKILL.md",
    "skill/zhangxiaojun-interview-question-designer/agents/openai.yaml",
    "skill/zhangxiaojun-interview-question-designer/references/sample_episode_pattern_library.md",
    "skill/zhangxiaojun-interview-question-designer/scripts/generate_interview_scaffold.py",
    "dist/zhangxiaojun-interview-question-designer.skill",
]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    sys.exit(1)


def validate_required_files() -> None:
    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.exists():
            fail(f"Missing required file: {rel}")


def validate_skill_frontmatter() -> None:
    skill_md = SKILL_DIR / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        fail("SKILL.md has no YAML frontmatter block")
    frontmatter = match.group(1)
    if "name: zhangxiaojun-interview-question-designer" not in frontmatter:
        fail("SKILL.md frontmatter has unexpected name")
    if "description:" not in frontmatter:
        fail("SKILL.md frontmatter is missing description")


def validate_python_syntax() -> None:
    for script in (SKILL_DIR / "scripts").glob("*.py"):
        ast.parse(script.read_text(encoding="utf-8"), filename=str(script))


def validate_no_ds_store() -> None:
    for path in ROOT.rglob(".DS_Store"):
        fail(f"Remove macOS metadata file: {path.relative_to(ROOT)}")


def main() -> None:
    validate_required_files()
    validate_skill_frontmatter()
    validate_python_syntax()
    validate_no_ds_store()
    print("Repository validation passed.")


if __name__ == "__main__":
    main()

