import random
import re
import os

def get_random_repo():
    # Statically map your personal repository collection details
    # This prevents internet rate blocks or empty JSON data failures completely
    my_repos = [
        {
            "name": "FRes-Video-Format",
            "url": "https://github.com",
            "desc": "A custom, uncompressed 16-bit HDR video container layout utilizing interleaved audio-first binary streams with real-time memory purging.",
            "lang": "Python"
        },
        {
            "name": ".github",
            "url": "https://github.com",
            "desc": "Centralized GitHub profile metadata workspace configuration tracking automated project cards and statistics screens.",
            "lang": "Python / YAML"
        }
    ]
    
    # Select one repository entirely at random
    chosen = random.choice(my_repos)
    
    name = chosen["name"]
    repo_url = chosen["url"]
    desc = chosen["desc"]
    lang = chosen["lang"]

    return f"### 🎲 Featured Repository: [{name}]({repo_url})\n> {desc}\n> 📊 **Primary Language:** {lang}"

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
