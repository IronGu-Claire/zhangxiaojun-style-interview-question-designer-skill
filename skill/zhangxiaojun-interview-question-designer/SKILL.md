---
name: zhangxiaojun-interview-question-designer
description: "Generate high-quality Chinese technology interview question plans inspired by Zhang Xiaojun's long-form interview craft. Use when the user provides a guest name, role, company, topic, background notes, transcript, article, or links and wants 张小珺式访谈问题, 科技采访提纲, 深度访谈问题, 创始人/AI/投资/产品访谈大纲, or follow-up question trees."
---

# Zhang Xiaojun Interview Question Designer

Use this skill to design **deep, sharp, complete Chinese interview questions** for technology, AI, startup, product, investment, and business interviews. The goal is not generic Q&A; the goal is a long-form interview plan with strong framing, clear arcs, productive follow-ups, and enough depth for a 2-6 hour conversation.

## Input Contract

The user may provide any subset of:

- guest name, title, company, field, and public links;
- interview goal, target audience, desired length, sensitive boundaries;
- background notes, previous transcript, article, deck, product docs, or topic list.

If key context is missing, proceed with reasonable assumptions and mark them as `待确认`. For current facts about people, companies, products, funding, launches, roles, or public controversies, verify from reliable sources before relying on them. Cite source links when research is used.

## Default Output

Unless the user asks for a different format, produce a Markdown interview plan with:

1. `采访定位`: one paragraph on the interview's core thesis and audience promise.
2. `嘉宾画像与信息缺口`: confirmed facts, plausible hypotheses, and what needs verification.
3. `时长与节奏`: default to 180 minutes unless the user specifies otherwise; include 120/180/240 minute cuts when useful.
4. `主线结构`: 6-10 sections in interview order, each with its purpose and time budget.
5. `核心问题清单`: 28-60 questions, grouped by section.
6. `追问树`: 12-25 conditional follow-ups for evasive, surprising, technical, or vague answers.
7. `必问硬问题`: 8-15 respectful but non-softball questions.
8. `收束问题`: 5-8 questions that produce reflection, judgment, and forward-looking insight.

Add a compact `使用提示` only when helpful: how to choose questions for a 120/180/240-minute interview.

## Optional Scripts

Use these scripts when they improve reliability or when the user wants reusable artifacts:

```bash
python3 SKILL_DIR/scripts/generate_interview_scaffold.py \
  --guest "嘉宾姓名" \
  --background "一段背景信息" \
  --topic "采访主题" \
  --duration-minutes 180 \
  --archetype auto \
  --out "WORK_DIR/嘉宾-张小珺式深访提纲骨架.md"
```

```bash
python3 SKILL_DIR/scripts/audit_question_plan.py \
  --input "WORK_DIR/采访提纲.md" \
  --out "WORK_DIR/采访提纲-质量检查.md"
```

```bash
python3 SKILL_DIR/scripts/extract_question_patterns.py \
  --input "WORK_DIR/张小珺访谈文字稿.md" \
  --out "WORK_DIR/提问模式抽取.md"
```

The scripts do not replace judgment. Use them to scaffold, audit, or learn patterns, then write the final question plan with the method references.

## Workflow

### 1. Build The Interview Thesis

Turn background into one central tension:

- What changed in the guest's world?
- Why now?
- What did the guest see earlier, do differently, or learn the hard way?
- Which belief, strategy, product, model, market, or organization is being tested?

Do not start by listing biographical questions. Start from the most interesting live problem.

### 2. Map The Guest

Create a concise map:

- public role and recent milestones;
- technical/product/business domain;
- decisions the guest likely made personally;
- controversies, constraints, or unproven claims;
- concepts that need translation for a smart non-specialist audience.

Separate `已知事实`, `合理推断`, and `待确认`.

### 3. Select The Episode Archetype

Read `references/sample_episode_pattern_library.md` when the guest resembles one of the seed cases:

- AI researcher / Agent scholar: 姚顺雨.
- top-lab research scientist with strong personal voice: 姚顺宇.
- technical founder / returning guest: 杨植麟.
- AI Lab technical leader during a paradigm shift: 罗福莉.
- CEO operator / product strategist: 李想.
- robotics scientist / embodied AI lead: 谭捷.
- oral-history founder crossing academia, industry, VC, and entrepreneurship: 余凯.
- year-end macro investor: 戴雨森.
- public-market / Silicon Valley investor: Freda.
- serial realist VC / contrarian market observer: 朱啸虎.

Use the closest archetype to shape the arc, but do not copy a previous episode. The output must be guest-specific.

### 4. Design Zhang Xiaojun-Style Questions

Read `references/zhangxiaojun_question_method.md` when generating the actual questions. Apply these principles:

- Use long-form framing when it increases precision: context + observed contradiction + direct ask.
- Prefer mechanism questions over opinion questions.
- Ask for concrete episodes, decisions, tradeoffs, numbers, before/after changes, and wrong turns.
- Move across levels: personal experience -> product/technology -> organization -> industry structure -> future judgment.
- Preserve intellectual pressure while keeping the tone curious and respectful.

### 5. Set Long-Form Timing

Read `references/longform_duration_design.md` before choosing the plan length. Default to:

- `180 minutes`: normal Zhang Xiaojun-style deep interview.
- `240 minutes`: technical founder, AI researcher, product leader, or complex company story.
- `120 minutes`: shortened version when the user has a hard limit.
- `360 minutes`: documentary-level archive interview with multiple life/work chapters.

Avoid treating 30/60 minutes as the default; those are extraction cuts, not the core plan.

### 6. Choose The Output Template

Read `references/question_output_templates.md` when the user needs:

- a full interview script;
- a 120/180/240/360-minute plan;
- question cards for live hosting;
- a pre-interview research brief;
- a guest-specific question bank.

### 7. Quality Bar

Before finalizing, check:

- The questions are specific to this guest, not reusable boilerplate.
- At least one section examines the guest's actual decisions or work product.
- At least one section probes uncertainty, failure, tradeoff, or disagreement.
- Technical questions are understandable without dumbing down the topic.
- Follow-ups can recover depth if the guest answers vaguely.
- No unverified claim is stated as fact.

## Style Rules

- Write in polished Chinese, suitable for a professional host's preparation notes.
- Keep questions natural enough to say aloud.
- Use `你` unless the user's context calls for a more formal address.
- Avoid flattery-only questions and vague prompts like “你怎么看未来”.
- Do not imitate a person verbatim; extract reusable interview craft and structure.
