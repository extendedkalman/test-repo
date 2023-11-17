import requests
import os

repo_owner = "extendedkalman"
repo_name = "test-repo"

# Personal Access Token (PAT)
token = "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"

runner_name = "yalin-Yoga-Slim-7-ProX-14IAH7"

# GitHub API endpoint
api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runners"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}

response_stop = requests.post(f"{api_url}/remove-token", headers=headers, json={"runner_name": runner_name})

if response_stop.status_code == 204:
    print(f"{runner_name} self-hosted runner successfly stoppped.")
else:
    print(f"error: {response_stop.status_code} - {response_stop.text}")