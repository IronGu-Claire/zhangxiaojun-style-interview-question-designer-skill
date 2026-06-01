# Usage Guide

## 1. Install the skill

```bash
mkdir -p ~/.codex/skills
cp -R skill/zhangxiaojun-interview-question-designer ~/.codex/skills/
```

After installation, invoke it in Codex with `$zhangxiaojun-interview-question-designer`.

## 2. Minimal prompt

```text
Use $zhangxiaojun-interview-question-designer to create a Zhang Xiaojun-style deep interview plan for Guest Name.
Background: guest role, company, product, field, and recent events.
Target length: 180 minutes.
```

## 3. Recommended input fields

- Guest name
- Role and organization
- Interview topic
- Target audience
- Target length
- Recent events or product launches
- Sensitive boundaries
- Questions you especially want to probe

## 4. Script usage

```bash
python3 skill/zhangxiaojun-interview-question-designer/scripts/generate_interview_scaffold.py \
  --guest "Tang Jie" \
  --background "Zhipu AI, GLM, large model company, open/closed source strategy, Agentic LLM" \
  --topic "Zhipu, GLM, and Chinese foundation model strategy" \
  --duration-minutes 180 \
  --archetype auto \
  --out examples/tang-jie-scaffold.md
```

## 5. Audit an output

```bash
python3 skill/zhangxiaojun-interview-question-designer/scripts/audit_question_plan.py \
  --input examples/tang-jie-scaffold.md
```

## 6. What a good output should contain

- A clear interview thesis.
- A guest map with known facts, hypotheses, and gaps.
- A long-form timing plan.
- Sectioned questions specific to the guest.
- Follow-up trees for vague or evasive answers.
- Respectful but real hard questions.
- Reflective closing questions.

