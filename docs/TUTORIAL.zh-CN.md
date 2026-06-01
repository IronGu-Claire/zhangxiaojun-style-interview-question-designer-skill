# 完整教程：从嘉宾背景到深访提纲

## Step 1：准备背景

至少准备三类信息：

- 嘉宾是谁：姓名、身份、组织、代表作品。
- 为什么现在访：近期发布、争议、技术变化、公司节点。
- 想问出什么：技术路线、产品化、组织、商业化、个人判断，还是行业趋势。

## Step 2：选择或自动识别嘉宾原型

skill 支持 `--archetype auto` 自动识别，也可以手动指定：

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

## Step 3：生成提纲骨架

```bash
python3 skill/zhangxiaojun-interview-question-designer/scripts/generate_interview_scaffold.py \
  --guest "嘉宾姓名" \
  --background "背景信息" \
  --topic "采访主题" \
  --duration-minutes 180 \
  --archetype auto \
  --out examples/interview-plan.md
```

## Step 4：把骨架变成正式访纲

用 Codex 调用 skill：

```text
请使用 $zhangxiaojun-interview-question-designer，基于 examples/interview-plan.md，生成一份正式的张小珺式深度访谈提纲。
要求：问题要结合嘉宾真实背景；不要泛泛而谈；保留 180 分钟节奏；加入追问树和硬问题。
```

## Step 5：做质量检查

```bash
python3 skill/zhangxiaojun-interview-question-designer/scripts/audit_question_plan.py \
  --input examples/interview-plan.md
```

## Step 6：人工复核

正式采访前，请人工核实：

- 嘉宾头衔和公司信息是否最新。
- 技术产品名是否正确。
- 商业和融资信息是否可公开。
- 问题是否触碰保密边界。
- 硬问题是否尖锐但尊重。

