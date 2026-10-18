import random
import re
import urllib.request
import json
import os

def get_random_repo():
    url = "https://github.com"
    
    # Securely retrieve the GitHub Actions security token from the server engine environment
    token = os.environ.get("GITHUB_TOKEN")
    
    headers = {'User-Agent': 'Python-Script'}
    if token:
        # Inject authentication headers to elevate rate limits to 1,000 requests/hr
        headers['Authorization'] = f"token {token}"
        
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req) as response:
            repos = json.loads(response.read().decode())
    except Exception as e:
        return f"<!-- Error fetching repositories: {e} -->"
    
    # Filter out forks and your meta configuration repository
    public_repos = [r for r in repos if not r['fork'] and r['name'] != '.github']
    
    if not public_repos:
        return "### 🎲 Featured Repository\n> No public repository variants discovered yet!"
        
    chosen = random.choice(public_repos)
    name = chosen['name']
    repo_url = chosen['html_url']
    desc = chosen['description'] if chosen['description'] else "No project description provided yet."
    stars = chosen['stargazers_count']
    lang = chosen['language'] if chosen['language'] else "Mixed / Polyglot"

    return f"### 🎲 Featured Repository: [{name}]({repo_url})\n> {desc}\n> 📊 **Primary Language:** {lang} | ⭐ **Stars:** {stars}"

def update_readme():
    readme_path = "profile/README.md"
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_repo_markdown = get_random_repo()
    pattern = r"(<!-- RANDOM-REPO:START -->)(.*?)(<!-- RANDOM-REPO:END -->)"
    updated_content = re.sub(pattern, f"\\1\n{new_repo_markdown}\n\\3", content, flags=re.DOTALL)
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

if __name__ == "__main__":
    update_readme()
