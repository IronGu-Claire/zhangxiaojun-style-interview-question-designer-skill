#!/usr/bin/env python3
"""Generate a structured long-form interview plan scaffold."""

from __future__ import annotations

import argparse
from pathlib import Path


ARCS = {
    120: [
        ("0-10", "开场：最近变化与核心矛盾"),
        ("10-30", "个人转折与时间线"),
        ("30-60", "机制拆解：技术/产品/市场"),
        ("60-85", "真实决策、失败与取舍"),
        ("85-105", "组织与行业结构"),
        ("105-120", "未来判断与收束"),
    ],
    180: [
        ("0-12", "开场：最近变化、核心矛盾、为什么是这个嘉宾"),
        ("12-35", "个人判断形成：第一次意识到变化的时刻"),
        ("35-70", "机制拆解：技术/产品/市场如何互相推动"),
        ("70-100", "具体决策：路线、失败、取舍、反对意见"),
        ("100-125", "组织系统：人才、激励、资源分配"),
        ("125-150", "竞争与外界质疑：行业结构、风险、误解"),
        ("150-170", "未来判断：信号、反共识、可证伪条件"),
        ("170-180", "个人反思与最后一问"),
    ],
    240: [
        ("0-15", "开场：核心论题与时代变化"),
        ("15-45", "时间线：品味形成、早期信号、关键转折"),
        ("45-90", "深度机制：技术/产品/市场/用户真实需求"),
        ("90-125", "实验与失败：决策日志、错误路线、代价"),
        ("125-155", "商业化与分发：用户、价格、渠道、留存"),
        ("155-185", "组织与资源：招聘、激励、算力/资本/注意力"),
        ("185-215", "竞争、争议与风险：外界最强质疑"),
        ("215-235", "未来场景：非共识判断与验证信号"),
        ("235-240", "收束：个人反思"),
    ],
    360: [
        ("0-20", "开场：时代变化与核心问题"),
        ("20-60", "个人经历与世界观"),
        ("60-110", "关键机制：技术/产品/市场"),
        ("110-155", "项目或公司发展时间线"),
        ("155-200", "关键决策、失败与取舍"),
        ("200-245", "组织、人才、资源配置"),
        ("245-285", "行业结构、资本、竞争"),
        ("285-325", "争议、风险、反共识"),
        ("325-350", "未来判断"),
        ("350-360", "个人反思和最后一问"),
    ],
}

ARCHETYPES = {
    "auto": "auto",
    "ai-lab-leader": "AI Lab 技术负责人",
    "agent-researcher": "Agent 研究者",
    "frontier-lab-scientist": "前沿实验室研究科学家",
    "technical-founder": "技术创始人",
    "ceo-operator": "CEO / 产品战略家",
    "robotics-scientist": "机器人 / Embodied AI 科学家",
    "oral-history-founder": "口述史型创始人",
    "macro-vc": "年度复盘型 VC",
    "public-market-investor": "美股 / 硅谷投资人",
    "serial-realist-vc": "连续追踪型现实主义 VC",
}

ARCHETYPE_KEYWORDS = {
    "agent-researcher": ["agent", "智能体", "openai", "强化学习", "评估", "任务定义", "姚顺雨"],
    "frontier-lab-scientist": ["deepmind", "anthropic", "gemini", "前沿实验室", "研究科学家", "物理", "姚顺宇"],
    "technical-founder": ["创始人", "kimi", "moonshot", "模型公司", "开源", "闭源", "杨植麟"],
    "ceo-operator": ["ceo", "产品战略", "理想", "汽车", "组织", "家庭", "李想"],
    "robotics-scientist": ["机器人", "具身", "embodied", "world model", "世界模型", "跨本体", "谭捷"],
    "oral-history-founder": ["30年", "口述史", "地平线", "余凯", "学术", "江湖"],
    "macro-vc": ["年终", "复盘", "预期", "真格", "戴雨森", "融资", "return", "research", "memory"],
    "public-market-investor": ["美股", "altimeter", "freda", "openai", "anthropic", "robinhood", "token"],
    "serial-realist-vc": ["朱啸虎", "泡沫", "aigc", "现实主义", "金沙江", "deepseek"],
}

ARCHETYPE_QUESTIONS = {
    "ai-lab-leader": [
        "这次范式变化最先打到你们系统里的哪一层：模型、数据、评估、工程，还是组织？",
        "你们后来重新分配了哪些资源：人、卡、数据、时间，还是注意力？",
        "哪个旧范式里的强项，在新范式里反而变成了包袱？",
        "你作为负责人，最需要亲自盯住的技术判断是什么？",
        "如果外界只看到发布结果，最容易漏掉你们内部哪类艰难工作？",
    ],
    "agent-researcher": [
        "你会怎么定义这个领域的最小闭环：模型、环境、任务、反馈分别是什么？",
        "Agent 的难点是在能力、环境、任务定义，还是评估标准？",
        "如果创业者误读你的研究，最可能误读成什么？",
        "语言模型之后，Agent 和过去的自动化系统本质差别在哪里？",
        "人的边界、系统边界和产品边界分别会怎么移动？",
    ],
    "frontier-lab-scientist": [
        "你这个判断听起来很反直觉，它背后的第一性原理是什么？",
        "哪些事情外界会归功于天才个体，但内部其实是系统工程？",
        "你从物理转到 AI 后，哪种训练方式反而最有用？",
        "前沿实验室真正的竞争力是算法、数据、算力、工程，还是问题定义？",
        "英雄主义过去之后，什么样的研究员会变得更重要？",
    ],
    "technical-founder": [
        "如果把你上一阶段最重要的判断拿出来复盘，哪一个今天要改写？",
        "新模型/新产品到底证明的是能力、效率、工程化，还是市场路径？",
        "你现在更像在做模型公司、产品公司，还是基础设施公司？",
        "开源/闭源、平台/产品、增长/收入之间，最难的取舍是哪一个？",
        "公司的技术品味怎么变成组织能力，而不是只停留在创始人身上？",
    ],
    "ceo-operator": [
        "如果把你当成一个 CEO 大模型，你现在的输入、训练数据和奖励函数是什么？",
        "这个技术判断从战略落到产品时，最容易在哪一层失真？",
        "你怎么判断这是用户生活里的真实需求，而不是技术团队兴奋的能力？",
        "组织要学会这件事，最先需要改变的是流程、人才，还是决策权？",
        "你自己过去哪条管理经验，在 AI 阶段需要被重训？",
    ],
    "robotics-scientist": [
        "机器人今天到底是模型问题、数据问题、硬件问题，还是任务定义问题？",
        "跨本体迁移真正迁移的是什么：视觉、动作、常识，还是任务结构？",
        "一个机器人 demo 什么时候才算从研究结果变成产品能力？",
        "LLM 给机器人带来的变化，哪些是真变化，哪些只是表达方式变了？",
        "未来五到十年，机器人最可能先在哪个场景穿透？",
    ],
    "oral-history-founder": [
        "如果把这段经历压成几次判断升级，每一次升级分别因为什么发生？",
        "你说企业的核心竞争力是品味，品味具体体现在哪些不可外包的判断上？",
        "哪些当年看起来像江湖故事的选择，后来变成了战略能力？",
        "你从学术、产业、投资、创业之间切换时，最难迁移的能力是什么？",
        "物理世界 AI 最终要给人带来的自由，具体是什么自由？",
    ],
    "macro-vc": [
        "如果把今年拆成技术、应用、融资、情绪四条曲线，哪条最超预期？",
        "你提出的年度关键词，分别要用什么指标验证？",
        "泡沫如果存在，会先从估值、用户留存、收入质量，还是算力支出里露出来？",
        "对创业者来说，明年最大的窗口和最大的幻觉分别是什么？",
        "你自己的投资框架里，哪一条今年被迫更新了？",
    ],
    "public-market-investor": [
        "这个市场现在奖励的是增长、效率、稀缺性，还是叙事控制力？",
        "Token 消耗和真实价值之间，哪一层开始脱钩了？",
        "AI 时代软件公司的脆弱性，最先会体现在产品、组织，还是财务指标上？",
        "美股投资人看 OpenAI/Anthropic 这类公司，和创业投资人最大的差别是什么？",
        "你的投资流程里，哪些信息交换已经可以交给 AI，哪些还必须靠人的判断？",
    ],
    "serial-realist-vc": [
        "你上一次最重要的判断，今天要改哪一条？哪一条反而更确定？",
        "大家都在讲 AI Bubble，你觉得真正的泡沫应该在哪个指标上出现？",
        "如果中国要出现千亿美金 AI 应用机会，它最可能长在哪个入口和商业模式上？",
        "大厂更大和创业公司有机会，这两个判断怎么同时成立？",
        "如果你今天重新做一支 AI 组合，哪些方向会完全不碰？",
    ],
}


def nearest_duration(minutes: int) -> int:
    return min(ARCS, key=lambda preset: abs(preset - minutes))


def resolve_archetype(raw_archetype: str, guest: str, background: str, topic: str) -> str:
    if raw_archetype != "auto":
        return raw_archetype
    haystack = f"{guest} {background} {topic}".lower()
    scores: dict[str, int] = {}
    for archetype, keywords in ARCHETYPE_KEYWORDS.items():
        scores[archetype] = sum(1 for keyword in keywords if keyword.lower() in haystack)
    best, score = max(scores.items(), key=lambda item: item[1])
    return best if score > 0 else "technical-founder"


def section_questions(section: str) -> list[str]:
    if "开场" in section:
        return [
            "如果只用一个最近发生的变化来解释你现在所处的位置，你会选哪个变化？",
            "外界通常怎么理解这件事？你觉得这个理解里最关键的偏差是什么？",
            "这次访谈我想抓住的核心矛盾是：____。你会怎么修正这个提法？",
        ]
    if "反思" in section or "收束" in section or "最后一问" in section:
        return [
            "这段经历对你个人最大的改变是什么？",
            "如果几年后回看今天，你希望自己没有忽略哪件事？",
            "最后，如果只能留下一个判断给这个行业，你会说什么？",
        ]
    if "个人" in section or "时间线" in section:
        return [
            "你第一次意识到这件事不再按旧逻辑运行，是在哪个具体时刻？",
            "如果把你的判断变化切成几个阶段，分界点分别是什么？",
            "过去哪段经历今天看起来被重新解释了？",
        ]
    if "机制" in section:
        return [
            "如果拆到底层机制，这件事到底是哪一层先变了？",
            "这个机制里最容易被外界误读的因果关系是什么？",
            "有没有一个具体案例能说明它不是概念变化，而是真实能力变化？",
        ]
    if "决策" in section or "失败" in section:
        return [
            "当时桌上有哪些路线？你们为什么选了现在这条？",
            "有没有一个看起来正确、后来被你们放弃的判断？",
            "这个决策最贵的成本是什么：时间、钱、人才、算力、注意力，还是窗口期？",
        ]
    if "组织" in section or "资源" in section:
        return [
            "这个变化对组织结构提出了什么新要求？",
            "什么样的人在这个阶段突然变得更重要？",
            "如果资源只能投三件事，你会怎么排优先级？",
        ]
    if "竞争" in section or "争议" in section or "风险" in section:
        return [
            "外界对你们最大的质疑是什么？哪一条你认为是有道理的？",
            "如果你的判断错了，最可能错在哪里？",
            "这个行业现在最大的伪共识是什么？",
        ]
    if "未来" in section:
        return [
            "未来 12-24 个月，最能验证你判断的三个信号是什么？",
            "哪个今天看起来很热的方向，你认为可能被证明没那么重要？",
            "如果这轮变化真的成立，行业分工会怎么重排？",
        ]
    return [
        "这个阶段最值得问清楚的事实是什么？",
        "这里面最大的误解是什么？",
        "能不能给一个具体例子？",
    ]


def build_markdown(args: argparse.Namespace) -> str:
    duration = nearest_duration(args.duration_minutes)
    arc = ARCS[duration]
    background = args.background.strip() or "待补充"
    topic = args.topic.strip() or "待确认核心主题"
    guest = args.guest.strip()
    archetype = resolve_archetype(args.archetype, guest, background, topic)
    archetype_label = ARCHETYPES[archetype]

    lines = [
        f"# {guest}：张小珺式深度访谈提纲骨架",
        "",
        "## 采访定位",
        "",
        f"- 嘉宾：{guest}",
        f"- 主题：{topic}",
        f"- 建议时长：{duration} 分钟",
        f"- 访谈原型：{archetype_label}",
        f"- 背景：{background}",
        "",
        "这次访谈不要从履历平铺开始，而要从嘉宾身上正在发生的变化、争议或判断切入，逐层追到机制、决策、组织和未来信号。",
        "",
        "## 嘉宾画像与信息缺口",
        "",
        "- 已知事实：待根据公开资料核实。",
        "- 合理推断：待从背景信息中提炼。",
        "- 待确认：职位、最近项目、关键时间点、可公开讨论边界。",
        "",
        "## 时长与主线结构",
        "",
    ]
    for time_range, section in arc:
        lines.append(f"- {time_range} min：{section}")

    lines.extend(["", "## 核心问题清单", ""])
    for index, (time_range, section) in enumerate(arc, start=1):
        lines.extend([f"### {index}. {section}（{time_range} min）", ""])
        for q_index, question in enumerate(section_questions(section), start=1):
            lines.append(f"{q_index}. {question}")
        lines.append("")

    lines.extend(["## 原型专属问题", ""])
    for index, question in enumerate(ARCHETYPE_QUESTIONS.get(archetype, []), start=1):
        lines.append(f"{index}. {question}")
    lines.append("")

    lines.extend(
        [
            "## 追问树",
            "",
            "- 如果回答很抽象：能不能落到一个具体场景、一次会议、一个指标或一个用户反馈？",
            "- 如果只讲结果不讲过程：当时中间经历了哪几个判断步骤？哪一步最不确定？",
            "- 如果回避失败：有没有一个现在看起来不该那么做的选择？",
            "- 如果给出反常判断：这个判断最强的反方证据是什么？",
            "- 如果技术解释过深：如果讲给一个聪明但非本领域的人，最短的解释是什么？",
            "",
            "## 必问硬问题",
            "",
            "1. 外界对你/你们这件事最强的质疑是什么？",
            "2. 这个判断如果错了，最可能错在哪个前提？",
            "3. 你们有没有把技术能力误判成产品能力，或者把短期热度误判成长期趋势？",
            "4. 哪些结果现在还没有被证明，所以不能讲得太满？",
            "5. 如果把成功归因拆开，哪一部分是能力，哪一部分是时机？",
            "",
            "## 收束问题",
            "",
            "1. 未来 12-24 个月，你最希望外界观察哪几个信号？",
            "2. 今天这个行业里，哪一个共识最可能被改写？",
            "3. 如果几年后回看这段时间，你觉得它更像一个泡沫、一场范式转移，还是两者同时存在？",
            "4. 这件事对你个人最大的改变是什么？",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--guest", required=True, help="Guest name")
    parser.add_argument("--background", default="", help="Short guest background")
    parser.add_argument("--topic", default="", help="Interview topic")
    parser.add_argument("--duration-minutes", type=int, default=180)
    parser.add_argument(
        "--archetype",
        default="auto",
        choices=sorted(ARCHETYPES),
        help="Interview archetype; use auto to infer from guest/background/topic",
    )
    parser.add_argument("--out", required=True, help="Output Markdown path")
    args = parser.parse_args()

    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_markdown(args), encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
