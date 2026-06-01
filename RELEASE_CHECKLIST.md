# Release Checklist

Use this before publishing a GitHub release.

- [ ] Confirm `skill/zhangxiaojun-interview-question-designer/SKILL.md` has valid frontmatter.
- [ ] Run `python3 tools/validate_repo.py`.
- [ ] Run at least one scaffold example with `--archetype auto`.
- [ ] Run `audit_question_plan.py` on the example output.
- [ ] Rebuild `dist/zhangxiaojun-interview-question-designer.skill`.
- [ ] Confirm README links work.
- [ ] Confirm examples do not contain private notes, private transcripts, API keys, or unpublished interview material.
- [ ] Add a changelog entry.
- [ ] Create a GitHub release tag, for example `v0.1.0`.

