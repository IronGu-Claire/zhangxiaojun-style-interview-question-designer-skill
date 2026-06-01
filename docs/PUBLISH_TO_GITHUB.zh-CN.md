# 发布到 GitHub

## 推荐仓库名

```text
zhangxiaojun-style-interview-question-designer-skill
```

## 推荐简介

```text
A Codex skill for generating Zhang Xiaojun-style long-form Chinese technology interview question plans.
```

## 推荐 Topics

```text
codex-skill
interview
chinese
ai
technology
podcast
zhangxiaojun
question-generation
prompt-engineering
```

## 初始化仓库

```bash
git init
git add .
git commit -m "Initial public release"
git branch -M main
git remote add origin git@github.com:YOUR_NAME/zhangxiaojun-style-interview-question-designer-skill.git
git push -u origin main
```

## 发布前检查

```bash
python3 tools/validate_repo.py
```

检查通过后，再创建 GitHub release，上传 `dist/zhangxiaojun-interview-question-designer.skill` 作为 release artifact。

