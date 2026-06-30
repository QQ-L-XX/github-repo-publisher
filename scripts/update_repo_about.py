#!/usr/bin/env python3
"""Update GitHub repository About metadata without printing tokens."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request


def run_quiet(command: list[str], input_text: str | None = None) -> str | None:
    try:
        completed = subprocess.run(
            command,
            input=input_text,
            text=True,
            capture_output=True,
            check=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    return completed.stdout.strip()


def token_from_git_credentials() -> str | None:
    output = run_quiet(
        ["git", "credential", "fill"],
        "protocol=https\nhost=github.com\n\n",
    )
    if not output:
        return None
    for line in output.splitlines():
        if line.startswith("password="):
            return line.split("=", 1)[1].strip()
    return None


def get_token() -> str:
    for name in ("GITHUB_TOKEN", "GH_TOKEN"):
        value = os.environ.get(name)
        if value:
            return value

    gh_token = run_quiet(["gh", "auth", "token"])
    if gh_token:
        return gh_token

    credential_token = token_from_git_credentials()
    if credential_token:
        return credential_token

    raise SystemExit(
        "No GitHub token found. Set GITHUB_TOKEN/GH_TOKEN, run gh auth login, "
        "or configure Git Credential Manager."
    )


def github_request(method: str, repo: str, token: str, payload: dict | None = None) -> dict:
    data = None
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    request = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "codex-github-repo-publisher-skill",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise SystemExit(f"GitHub API failed: HTTP {error.code}: {body}") from error


def main() -> int:
    parser = argparse.ArgumentParser(description="Update GitHub repository About metadata.")
    parser.add_argument("--repo", required=True, help="Repository in OWNER/REPO format.")
    parser.add_argument("--description", required=True, help="Bilingual GitHub About description.")
    parser.add_argument("--homepage", default="", help="Optional homepage URL.")
    parser.add_argument("--enable-issues", action="store_true", help="Enable GitHub Issues.")
    parser.add_argument("--enable-projects", action="store_true", help="Enable GitHub Projects.")
    parser.add_argument("--enable-wiki", action="store_true", help="Enable GitHub Wiki.")
    args = parser.parse_args()

    token = get_token()
    payload = {
        "description": args.description,
        "homepage": args.homepage,
        "has_issues": bool(args.enable_issues),
        "has_projects": bool(args.enable_projects),
        "has_wiki": bool(args.enable_wiki),
    }

    github_request("PATCH", args.repo, token, payload)
    repo = github_request("GET", args.repo, token)
    public = {
        "full_name": repo.get("full_name"),
        "description": repo.get("description"),
        "homepage": repo.get("homepage"),
        "html_url": repo.get("html_url"),
        "private": repo.get("private"),
    }
    print(json.dumps(public, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
