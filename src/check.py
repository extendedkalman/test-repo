import requests

# GitHub deposu ve iş akışı bilgileri
repo_owner = "extendedkalman"
repo_name = "test-repo"
workflow_name = "your_workflow"

# Personal Access Token (PAT)
token = "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"

# GitHub API endpoint
api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runners"

# Başlıklar
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}

# Çalışan işleri sorgula
response_running = requests.get(f"{api_url}/jobs?status=running", headers=headers)
running_jobs = response_running.json()["jobs"]

print("Çalışan İşler:")
for job in running_jobs:
    print(f"- Job ID: {job['id']}, Name: {job['name']}")

# Sırada bekleyen işleri sorgula
response_pending = requests.get(f"{api_url}/jobs?status=queued", headers=headers)
pending_jobs = response_pending.json()["jobs"]

print("\nSırada Bekleyen İşler:")
for job in pending_jobs:
    print(f"- Job ID: {job['id']}, Name: {job['name']}")