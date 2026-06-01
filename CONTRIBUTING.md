# Contributing

Thank you for considering a contribution.

## Good Contributions

- Improve interview archetypes.
- Add better example prompts or outputs.
- Improve Chinese/English documentation.
- Add validation checks.
- Fix bugs in helper scripts.
- Add references to public, verifiable interview materials.

## Contribution Rules

- Do not add private transcripts, private interview notes, API keys, or unpublished material.
- Do not add copyrighted long-form transcripts unless you have permission.
- Keep generated examples short enough to be reviewable.
- Mark unverified facts as `待确认` or `unverified`.
- Avoid impersonation. This skill extracts interview structure; it should not claim to be Zhang Xiaojun.

## Local Validation

```bash
python3 tools/validate_repo.py
```

## Pull Request Checklist

- [ ] README links still work.
- [ ] `SKILL.md` frontmatter is valid.
- [ ] Scripts pass syntax checks through `tools/validate_repo.py`.
- [ ] Examples do not include sensitive or private information.
- [ ] Changelog updated when behavior changes.
