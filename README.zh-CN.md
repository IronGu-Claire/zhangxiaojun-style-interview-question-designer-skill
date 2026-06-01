# 张小珺式深度访谈问题生成 Skill

这是一个面向 Codex Skills 的开源 skill，用来生成高质量中文科技深度访谈提纲。它不是普通“采访问题列表”，而是把张小珺式长访谈里的方法抽象出来：从嘉宾所处的变化、矛盾、技术路线、组织取舍、商业化和未来判断出发，生成可以直接拿来备采的结构化问题。

## 适合谁用

- 科技媒体、播客、视频访谈主持人
- AI / 大模型 / 创业 / 投资领域内容创作者
- 创始人访谈、产品访谈、投资人访谈、研究员访谈的备采人员
- 希望从“泛泛提问”升级到“深访追问结构”的人

## 核心能力

- 生成 120 / 180 / 240 / 360 分钟长访谈提纲。
- 输出采访定位、嘉宾画像、信息缺口、主线结构、核心问题、追问树、硬问题、收束问题。
- 支持多种嘉宾原型：AI Lab 技术负责人、Agent 研究者、前沿实验室科学家、技术创始人、CEO/产品战略家、机器人科学家、口述史型创始人、投资人等。
- 内置多期张小珺访谈样本模式，避免只套用某一期访谈。
- 附带脚本：生成骨架、审计提纲质量、从文字稿抽取提问模式。

## 安装

```bash
mkdir -p ~/.codex/skills
cp -R skill/zhangxiaojun-interview-question-designer ~/.codex/skills/
```

也可以使用 `dist/zhangxiaojun-interview-question-designer.skill` 作为打包分发文件。

## 快速使用

```text
请使用 $zhangxiaojun-interview-question-designer，为唐杰设计一份张小珺式深度访谈提纲。
背景：智谱，GLM，大模型公司，开源/闭源，Agentic LLM。
目标时长：180分钟。
```

## 输出应该长什么样

默认输出包含：

1. 采访定位
2. 嘉宾画像与信息缺口
3. 时长与节奏
4. 主线结构
5. 核心问题清单
6. 追问树
7. 必问硬问题
8. 收束问题

示例见：[examples/tang-jie-zhipu-glm.zh-CN.md](examples/tang-jie-zhipu-glm.zh-CN.md)

## 本 repo 的文件结构

```text
skill/zhangxiaojun-interview-question-designer/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/

docs/
  USAGE.zh-CN.md
  USAGE.en.md
  TUTORIAL.zh-CN.md
  TUTORIAL.en.md
  EVALUATION.zh-CN.md

examples/
  prompts.zh-CN.md
  prompts.en.md
  tang-jie-zhipu-glm.zh-CN.md
```

## 免责声明

本 skill 提取的是公开访谈中可复用的采访结构和问题方法，不用于模仿或冒充任何具体个人。生成内容需要使用者根据真实嘉宾背景、公开资料和采访边界进一步核实。

