# 张小珺式深度访谈问题生成 Skill

[English](README.en.md) | [简体中文完整说明](README.zh-CN.md)

这是一个面向 Codex Skills 的中文科技深度访谈问题生成工具。它不是简单罗列“采访问题”，而是把张小珺式长访谈中可复用的结构抽象出来：先找到嘉宾所处的时代变化和核心矛盾，再一路追到技术机制、产品取舍、组织能力、商业化、反方证据和未来判断。

你只需要输入嘉宾姓名和适当背景，它就可以生成一份适合 120 / 180 / 240 / 360 分钟长访谈使用的备采提纲，包括采访定位、主线结构、核心问题、追问树、必问硬问题和收束问题。


## 它能做什么

- 生成张小珺式中文科技深访提纲，而不是泛泛的 Q&A 列表。
- 支持 AI、大模型、创业、产品、投资、机器人、美股投资、创始人口述史等访谈场景。
- 默认按长访谈设计，支持 120、180、240、360 分钟节奏。
- 内置多期张小珺访谈样本原型，覆盖罗福莉、姚顺雨、姚顺宇、杨植麟、李想、谭捷、余凯、戴雨森、Freda、朱啸虎等嘉宾类型。
- 附带脚本，可生成访谈骨架、检查提纲质量、从已有文字稿中抽取提问模式。

## 目录结构

```text
.
├── skill/zhangxiaojun-interview-question-designer/  # Codex skill 源码
├── dist/zhangxiaojun-interview-question-designer.skill
├── docs/                                             # 使用教程与发布文档
├── examples/                                         # 示例提示词与效果样例
├── tools/                                            # 仓库校验工具
└── .github/                                          # Issue / PR 模板与 CI
```

## 快速开始

把 skill 复制到本机 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R skill/zhangxiaojun-interview-question-designer ~/.codex/skills/
```

然后在 Codex 中这样调用：

```text
请使用 $zhangxiaojun-interview-question-designer，为唐杰设计一份张小珺式深度访谈提纲。
背景：智谱，GLM，大模型公司，开源/闭源，Agentic LLM。
目标时长：180分钟。
```

## 文档

- [中文使用教程](docs/USAGE.zh-CN.md)
- [中文完整教程](docs/TUTORIAL.zh-CN.md)
- [效果评估方法](docs/EVALUATION.zh-CN.md)
- [发布到 GitHub](docs/PUBLISH_TO_GITHUB.zh-CN.md)
- [English usage guide](docs/USAGE.en.md)
- [English tutorial](docs/TUTORIAL.en.md)
- [发布检查清单](RELEASE_CHECKLIST.md)

## 效果示例

查看 [唐杰 / 智谱 / GLM 示例访纲](examples/tang-jie-zhipu-glm.zh-CN.md)，可以看到它如何把“智谱、GLM、开源/闭源、Agentic LLM”这样的背景，展开成一份 180 分钟长访谈提纲。

## 适用边界

这个 skill 提取的是公开访谈中可复用的采访结构和问题方法，不用于模仿或冒充任何具体个人。用于真实采访前，请继续核实嘉宾身份、公司信息、产品名称、可公开讨论边界和敏感事实。

## 开源协议

MIT License，详见 [LICENSE](LICENSE)。
