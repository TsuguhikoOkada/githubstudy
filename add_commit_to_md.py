# add_commit_to_md.py
from github import Github
import os
from datetime import datetime

# GitHub APIを利用するための認証
g = Github(os.getenv("GITHUB_TOKEN"))

# 現在のリポジトリを取得
repo = g.get_repo(os.getenv("GITHUB_REPOSITORY"))

# 最新のコミットを取得
commit = repo.get_commit(sha="develop") # develop branch
message = commit.commit.message

# 現在の日時を取得
now = datetime.now()

# ファイル名を生成 (yyyymmdd_hhmmss.md)
filename = now.strftime("%Y%m%d_%H%M%S.md")

# 最新のコミットメッセージをMarkdownファイルに保存
with open(filename, "w") as f:
    f.write(f"{message}\n")
