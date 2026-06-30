# Bilingual GitHub README Blueprint

Use this reference when creating or polishing a repository homepage.

## Recommended Structure

```markdown
<div align="center">

<img src="./images/logo.png" alt="Project Logo" width="96" />

# 中文名 · English Name

中文一句话价值主张。  
English one-line value proposition.

[Badges]

</div>

---

## 项目简介

Chinese overview: what the project is, who it is for, and what workflow it supports.

## Overview

English overview with the same practical meaning, not a word-for-word machine translation.

## 核心能力 / Features

| 模块 / Module | 能力 / Capability |
|---|---|
| 中文模块 / English module | 中文能力描述。English capability description. |

## 产品结构 / Product Structure

Chinese and English structure blocks when helpful.

## 技术架构 / Architecture

Mermaid diagram or concise stack explanation.

## 目录说明 / Directory Guide

Tree with short comments.

## 快速开始 / Quick Start

Install, configure, run, deploy, and test commands.

## 安全说明 / Security Notes

Explain secret handling, ignored local files, and pre-release checks.

## 软件著作权材料 / Copyright Registration Materials

State whether application materials are excluded from the public repo.

## 版本记录 / Changelog

Link to changelog if present.

## 许可证 / License

State license or unlicensed/private status.
```

## Writing Rules

- Put the project name and value proposition above the fold.
- Keep badges meaningful: platform, cloud/runtime, license, version.
- Translate intent, not every sentence mechanically.
- Avoid uploading private legal/copyright application files to a public repository.
- If the project is unlicensed, say that clearly in both languages.
- If generated materials are excluded by `.gitignore`, mention that in the README.
