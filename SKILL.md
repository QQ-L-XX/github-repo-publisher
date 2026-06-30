---
name: github-repo-publisher
description: Publish or polish a project on GitHub. Use when the user asks to create a new GitHub repository, connect an existing local project to GitHub, push code, write a beautiful repository README, update the GitHub About/description fields, or make the repository page bilingual in Chinese and English.
---

# GitHub Repo Publisher

## Overview

Use this skill to turn a local project into a polished GitHub repository page. The expected result is a pushed repository with a clear bilingual About description and a professional README that helps visitors understand, install, test, and evaluate the project.

## Workflow

1. Inspect the local project before changing anything:
   - `git status --short`
   - `git remote -v`
   - read `README.md`, `package.json`, app config, docs, and obvious entry points
   - identify project name, purpose, tech stack, run/test commands, license status, and security caveats

2. Clarify only when necessary:
   - Ask whether to create a new repo or use an existing repo if it cannot be inferred.
   - Ask whether the repo should be public or private before creating a new repository.
   - Do not ask if the user already provided the repo URL or name and requested execution.

3. Prepare the repository locally:
   - Initialize git only if the directory is not already a repo.
   - Respect unrelated user changes. Do not reset or overwrite them.
   - Add or update `.gitignore` for generated files, secrets, local config, build output, and private application materials.
   - Remove or quarantine hardcoded secrets before publishing.
   - Add meaningful package metadata when present, including repository URL and bilingual description when useful.

4. Build a polished bilingual README:
   - Read `references/readme-blueprint.md` when writing or heavily revising the README.
   - Keep the first viewport attractive: logo/title, one-line Chinese value proposition, one-line English value proposition, badges.
   - Include Chinese and English for the core sections, not only the title.
   - Prefer a structure visitors can scan: overview, features, architecture, directory guide, quick start, configuration, tests, security, copyright/materials note, changelog, license.
   - For public repos, avoid private application files, tokens, copyright application source bundles, or rendered registration materials.

5. Create or connect GitHub:
   - Prefer `gh` if installed and authenticated.
   - If `gh` is missing, use `git remote` and Git Credential Manager for pushing when available.
   - For creating a new repository without `gh`, use the GitHub REST API only with an explicit token from `GITHUB_TOKEN`, `GH_TOKEN`, or a credential manager.
   - Never print secrets in final messages. If a command output includes a token, do not repeat it to the user.

6. Commit and push:
   - Stage only relevant files.
   - Use a concise commit message, for example `docs: polish bilingual repository page` or `feat: publish project to github`.
   - Push to the intended branch, usually `main`.
   - If the remote has unrelated history, fetch and merge carefully instead of force pushing.

7. Update the GitHub About section:
   - Use `scripts/update_repo_about.py` when available.
   - Keep About concise and bilingual. Example:
     `听声记 / Voice Chat AI：智能语音记录微信小程序，支持录音、转写、AI 摘要、待办提取与好友语音通话 / A WeChat Mini Program for recording, transcription, AI summaries, todos, and friend voice calls.`
   - Verify the value by reading the repository back from the GitHub API.

8. Verify before reporting completion:
   - Run the project test command if available.
   - If the normal command is unavailable because Node/npm/Python is not on PATH, use bundled runtimes when available or state the exact blocker.
   - Confirm `git status --short` is clean unless there are intentional unrelated user changes.
   - Provide the repository URL, commit hash, About description, and test result.

## GitHub About Script

Use the bundled script to update repo metadata:

```bash
python path/to/github-repo-publisher/scripts/update_repo_about.py \
  --repo OWNER/REPO \
  --description "中文说明 / English description" \
  --homepage ""
```

Token lookup order:

1. `GITHUB_TOKEN`
2. `GH_TOKEN`
3. `gh auth token`
4. `git credential fill` for `https://github.com`

The script prints only public repo metadata and never prints the token.

## Quality Bar

- README is bilingual enough that a Chinese or English visitor can understand the project.
- GitHub About description is bilingual and concise.
- The repo does not publish generated copyright application materials unless the user explicitly asks.
- Secrets are absent from committed source.
- Pushed history is intentional and avoids destructive force pushes.
