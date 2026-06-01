# Tutorial: From Guest Background To Deep Interview Plan

## Step 1: Prepare context

Collect at least:

- Who the guest is: name, role, organization, representative work.
- Why now: recent launch, controversy, technical change, company milestone.
- What you want to uncover: technical route, productization, organization, commercialization, personal judgment, or industry trend.

## Step 2: Choose an archetype

Use `--archetype auto`, or choose one manually:

- `ai-lab-leader`
- `agent-researcher`
- `frontier-lab-scientist`
- `technical-founder`
- `ceo-operator`
- `robotics-scientist`
- `oral-history-founder`
- `macro-vc`
- `public-market-investor`
- `serial-realist-vc`

## Step 3: Generate a scaffold

```bash
python3 skill/zhangxiaojun-interview-question-designer/scripts/generate_interview_scaffold.py \
  --guest "Guest Name" \
  --background "Background notes" \
  --topic "Interview topic" \
  --duration-minutes 180 \
  --archetype auto \
  --out examples/interview-plan.md
```

## Step 4: Turn the scaffold into a polished plan

Ask Codex:

```text
Use $zhangxiaojun-interview-question-designer to turn examples/interview-plan.md into a polished Zhang Xiaojun-style long-form interview plan.
Keep the 180-minute rhythm, make questions guest-specific, add follow-up trees and hard questions.
```

## Step 5: Audit the plan

```bash
python3 skill/zhangxiaojun-interview-question-designer/scripts/audit_question_plan.py \
  --input examples/interview-plan.md
```

## Step 6: Human review

Before using the plan, verify:

- Current title and company facts.
- Product and technical terms.
- Public/private boundaries.
- Sensitive claims.
- Whether hard questions are precise and respectful.

