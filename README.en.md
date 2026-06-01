# Zhang Xiaojun-Style Interview Question Designer Skill

This repository contains a Codex skill for generating high-quality Chinese technology interview question plans. It is inspired by the structure of Zhang Xiaojun's long-form technology and business interviews, but it does not impersonate any person. It extracts reusable interview craft: thesis building, long-form arcs, mechanism questions, follow-up trees, hard questions, and reflective closing questions.

## Who This Is For

- Chinese technology interview hosts
- Podcast and video creators covering AI, startups, product, and investing
- Editorial teams preparing founder, researcher, CEO, investor, or product interviews
- Anyone who wants deeper interview questions than generic Q&A prompts

## Features

- Generates 120, 180, 240, or 360-minute long-form interview plans.
- Outputs interview thesis, guest map, information gaps, section arcs, core questions, follow-up trees, hard questions, and closing questions.
- Supports multiple guest archetypes: AI lab leader, Agent researcher, frontier-lab scientist, technical founder, CEO/product strategist, robotics scientist, oral-history founder, macro VC, public-market investor, and contrarian VC.
- Includes references extracted from multiple public Zhang Xiaojun interview patterns.
- Includes scripts for scaffolding, auditing, and extracting question patterns from transcripts.

## Install

```bash
mkdir -p ~/.codex/skills
cp -R skill/zhangxiaojun-interview-question-designer ~/.codex/skills/
```

You can also distribute the packaged file in `dist/zhangxiaojun-interview-question-designer.skill`.

## Quick Example

```text
Use $zhangxiaojun-interview-question-designer to create a Zhang Xiaojun-style deep interview plan for Tang Jie.
Background: Zhipu AI, GLM, large model company, open/closed source strategy, Agentic LLM.
Target length: 180 minutes.
```

## Documentation

- [Chinese usage guide](docs/USAGE.zh-CN.md)
- [English usage guide](docs/USAGE.en.md)
- [Chinese tutorial](docs/TUTORIAL.zh-CN.md)
- [English tutorial](docs/TUTORIAL.en.md)
- [Evaluation guide](docs/EVALUATION.zh-CN.md)

## License

MIT License. See [LICENSE](LICENSE).

