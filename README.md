<div align="center">

# GitHub Repo Publisher

一个用于发布、上传和美化 GitHub 仓库页面的 Codex Skill。  
A Codex skill for publishing projects to GitHub and polishing bilingual repository pages.

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827?style=for-the-badge)](#)
[![GitHub](https://img.shields.io/badge/GitHub-Publisher-181717?style=for-the-badge&logo=github)](#)
[![Python](https://img.shields.io/badge/Python-Utility-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-UNLICENSED-B56576?style=for-the-badge)](#)

</div>

---

## 项目简介

**GitHub Repo Publisher** 是一个 Codex Skill，用来把本地项目整理成一个专业的 GitHub 仓库。它覆盖从新建或绑定远程仓库、提交并推送代码，到编写精美中英文 README、更新 GitHub About 仓库说明、验证测试结果的完整流程。

这个 skill 适合用于需要“把项目发到 GitHub，并把仓库页面做好看、说明写清楚”的场景，尤其适合中文项目同时补齐英文介绍。

## Overview

**GitHub Repo Publisher** is a Codex skill for turning a local project into a polished GitHub repository. It covers creating or connecting a remote repository, committing and pushing the code, writing a professional bilingual README, updating the GitHub About description, and verifying the final result.

It is designed for requests such as “publish this project to GitHub,” “make the repository page look good,” or “add Chinese and English repository descriptions.”

## 核心能力 / Features

| 模块 / Module | 能力 / Capability |
|---|---|
| 仓库发布 / Repository publishing | 新建或绑定 GitHub 仓库，初始化 git，设置远程地址并推送代码。Create or connect a GitHub repository, initialize git, set the remote, and push the project. |
| 页面美化 / Page polish | 按项目特征整理 README，让仓库首页更清晰、更适合展示。Create a clear, attractive README tailored to the project. |
| 双语说明 / Bilingual copy | 同时写中文和英文的项目简介、功能说明、快速开始、安全说明和许可证说明。Write Chinese and English descriptions for overview, features, setup, security, and license sections. |
| About 更新 / About updates | 使用 GitHub API 更新仓库右侧 About 简介，支持中英文一句话说明。Update the repository About description through the GitHub API. |
| 发布验证 / Release checks | 推送后检查测试结果、git 状态、远程地址和公开仓库信息。Verify tests, git state, remotes, and public repository metadata after publishing. |
| 安全保护 / Safety guardrails | 避免上传密钥、私有配置、生成材料和无关临时文件。Avoid publishing secrets, local config, generated materials, or unrelated temporary files. |

## 目录说明 / Directory Guide

```text
.
├─ SKILL.md                         # Codex skill workflow and trigger metadata
├─ agents/
│  └─ openai.yaml                   # UI metadata for Codex skill discovery
├─ references/
│  └─ readme-blueprint.md           # Bilingual README structure and writing rules
└─ scripts/
   └─ update_repo_about.py          # GitHub About metadata updater
```

## 快速开始 / Quick Start

### 1. 安装 Skill / Install the Skill

把本仓库放到 Codex skills 目录中：

Place this repository under your Codex skills directory:

```text
C:\Users\<you>\.codex\skills\github-repo-publisher
```

或在其他系统中放到：

Or on other systems:

```text
~/.codex/skills/github-repo-publisher
```

### 2. 触发 Skill / Invoke the Skill

在 Codex 中直接说：

In Codex, ask:

```text
用 github-repo-publisher 把这个项目发到 GitHub，并做好中英文仓库页面
```

```text
Use github-repo-publisher to publish this project to GitHub and polish the bilingual repository page.
```

### 3. 更新 GitHub About / Update GitHub About

脚本会优先读取 `GITHUB_TOKEN`、`GH_TOKEN`、`gh auth token` 或 Git Credential Manager：

The script reads credentials from `GITHUB_TOKEN`, `GH_TOKEN`, `gh auth token`, or Git Credential Manager:

```bash
python scripts/update_repo_about.py \
  --repo OWNER/REPO \
  --description "中文仓库说明 / English repository description" \
  --enable-issues \
  --enable-projects
```

## 安全说明 / Security Notes

- 不要把 GitHub token、`.env`、本地私有配置或客户资料提交到仓库。
- 脚本不会打印 token，只会输出公开仓库元数据。
- 发布项目前应检查 `.gitignore`、运行测试，并确认没有硬编码密钥。

- Do not commit GitHub tokens, `.env` files, local private config, or customer data.
- The script does not print tokens; it only prints public repository metadata.
- Before publishing a project, review `.gitignore`, run tests, and confirm that no hardcoded secrets are present.

## 许可证 / License

当前仓库未声明开源许可证。未经授权请勿复制、分发或商用。

This repository does not currently declare an open-source license. Do not copy, distribute, or use it commercially without explicit permission.
