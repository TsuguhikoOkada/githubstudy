from github import Github
import os
import datetime

# Using an access token
g = Github(os.environ['GITHUB_TOKEN'])

# Get repo by name
repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])

# Get the sha of the most recent commit in the repository
latest_sha = repo.get_commits()[0].sha

# Get the commit object
commit = repo.get_git_commit(latest_sha)

# Get the commit message
message = commit.message

# Generate the filename
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"{timestamp}.md"

# Write the commit message to the markdown file
with open(filename, "w") as file:
    file.write(message)

print(f"Commit message saved to {filename}")
