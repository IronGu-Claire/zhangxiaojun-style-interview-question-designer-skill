# 原型烟雾测试

这些提示词用于检查 `--archetype auto` 是否能生成不同类型的访纲。

## 技术创始人

```bash
python3 skill/zhangxiaojun-interview-question-designer/scripts/generate_interview_scaffold.py \
  --guest "杨植麟" \
  --background "月之暗面创始人，Kimi，模型公司，开源闭源和Agentic LLM" \
  --topic "技术创始人的模型公司战略" \
  --duration-minutes 240 \
  --archetype auto \
  --out examples/yang-zhilin-scaffold.md
```

## CEO / 产品战略家

```bash
python3 skill/zhangxiaojun-interview-question-designer/scripts/generate_interview_scaffold.py \
  --guest "李想" \
  --background "理想汽车CEO，AI战略，产品战略，组织和家庭用户场景" \
  --topic "AI时代CEO如何重训自己和组织" \
  --duration-minutes 180 \
  --archetype auto \
  --out examples/li-xiang-scaffold.md
```

## 机器人科学家

```bash
python3 skill/zhangxiaojun-interview-question-designer/scripts/generate_interview_scaffold.py \
  --guest "谭捷" \
  --background "机器人科学家，Embodied AI，世界模型，跨本体迁移" \
  --topic "机器人与物理世界AI" \
  --duration-minutes 180 \
  --archetype auto \
  --out examples/tan-jie-scaffold.md
```

