from github import Github
import os
from datetime import datetime

g = Github(os.getenv("GH_TOKEN"))
repo = g.get_repo(os.getenv("GITHUB_REPOSITORY"))
commit = repo.get_commit(os.getenv("COMMIT_SHA"))
message = commit.commit.message

filename = datetime.now().strftime("%Y%m%d_%H%M%S.md")
with open(filename, "w") as f:
    f.write(f"Last commit: {message}")
