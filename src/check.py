import requests
import os

api_secret = os.environ.get('API_SECRET', None)

# GitHub deposu ve iş akışı bilgileri
repo_owner = "extendedkalman"
repo_name = "test-repo"
workflow_name = "hello world workflow"

# Personal Access Token (PAT)
token = api_secret

# GitHub API endpoint
api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runners"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}

response_running = requests.get(f"{api_url}/jobs?status=running", headers=headers)

print(f"response_running: {response_running}")

if response_running.status_code == 200:
    try:
        running_jobs = response_running.json()["jobs"]

        print("Running Jobs:")
        for job in running_jobs:
            print(f"- Job ID: {job['id']}, Name: {job['name']}")
    except KeyError as e:
        print(f"error: {e}")
else:
    print(f"error: {response_running.status_code} - {response_running.text}")

