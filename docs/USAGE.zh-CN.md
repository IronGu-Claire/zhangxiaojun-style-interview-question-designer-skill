# 使用指南

## 1. 安装 skill

```bash
mkdir -p ~/.codex/skills
cp -R skill/zhangxiaojun-interview-question-designer ~/.codex/skills/
```

安装后，在 Codex 中可以用 `$zhangxiaojun-interview-question-designer` 调用。

## 2. 最小可用提示词

```text
请使用 $zhangxiaojun-interview-question-designer，为嘉宾姓名设计一份张小珺式深度访谈提纲。
背景：嘉宾的身份、公司、产品、领域、近期事件。
目标时长：180分钟。
```

## 3. 推荐输入字段

- 嘉宾姓名
- 嘉宾身份和组织
- 采访主题
- 目标听众
- 目标时长
- 近期事件或产品
- 可公开讨论边界
- 希望重点追问的问题

## 4. 示例

```text
请使用 $zhangxiaojun-interview-question-designer，为唐杰设计一份张小珺式深度访谈提纲。
背景：智谱，GLM，大模型公司，开源/闭源，Agentic LLM。
目标时长：180分钟。
```

## 5. 使用脚本生成骨架

```bash
python3 skill/zhangxiaojun-interview-question-designer/scripts/generate_interview_scaffold.py \
  --guest "唐杰" \
  --background "智谱，GLM，大模型公司，开源/闭源，Agentic LLM" \
  --topic "智谱、GLM与中国大模型公司的技术路线" \
  --duration-minutes 180 \
  --archetype auto \
  --out examples/tang-jie-scaffold.md
```

## 6. 检查提纲质量

```bash
python3 skill/zhangxiaojun-interview-question-designer/scripts/audit_question_plan.py \
  --input examples/tang-jie-scaffold.md
```

## 7. 好结果的判断标准

- 不是泛泛问“你怎么看 AI 未来”。
- 有明确采访定位和核心矛盾。
- 问题能追到机制、取舍、具体场景、失败和反方证据。
- 有 120/180/240/360 分钟长访节奏。
- 能按嘉宾类型变化，而不是所有人都套同一套问题。

