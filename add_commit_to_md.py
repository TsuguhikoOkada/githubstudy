from github import Github
from datetime import datetime
import os

g = Github(os.getenv("GH_TOKEN"))
repo = g.get_repo(os.getenv("GITHUB_REPOSITORY"))
commit = repo.get_commit(os.getenv("GITHUB_SHA"))
message = commit.commit.message

date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
with open(f"{date_str}.md", "w") as f:
    f.write(message)
