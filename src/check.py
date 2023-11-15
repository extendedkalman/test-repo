import requests

# GitHub deposu ve iş akışı bilgileri
repo_owner = "extendedkalman"
repo_name = "test-repo"
workflow_name = "hello_world.yaml"

# Personal Access Token (PAT)
token = "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"

# GitHub API endpoint
api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runners"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}

# Çalışan işleri sorgula
response_running = requests.get(f"{api_url}/jobs?status=running", headers=headers)

# Yanıtın içeriğini kontrol et
if response_running.status_code == 200:
    try:
        running_jobs = response_running.json()["jobs"]
        print("Çalışan İşler:")
        for job in running_jobs:
            print(f"- Job ID: {job['id']}, Name: {job['name']}")
    except KeyError as e:
        print(f"Hata: JSON yapısında 'jobs' anahtarı bulunamadı. Detaylar: {e}")
else:
    print(f"Hata: {response_running.status_code} - {response_running.text}")