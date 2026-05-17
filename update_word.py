import json
import random
from datetime import datetime
import os
import requests

# Kelime havuzunu oku
with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

# Rastgele bir kelime seç
selected = random.choice(words)
today = datetime.now().strftime('%Y-%m-%d')

# Depo açıklaması için kısa ve net format (Kutu içinde görünecek yazı)
repo_description = f"🎯 {selected['word']}: {selected['meaning']}"

# 1. Gunun_Kelimesi.md dosyasını güncelle (YDS depon için)
with open('Gunun_Kelimesi.md', 'w', encoding='utf-8') as f:
    f.write(f"# 📝 Günün YDS Kelimesi ({today})\n\n## 🎯 **{selected['word']}**\n* **Anlamı:** {selected['meaning']}\n* **Örnek Cümle:** *{selected['example']}*")

# 2. GitHub API kullanarak deponun 'About/Description' kısmını güncelle
# GitHub Actions içindeki şifreli tokenı kullanıyoruz
token = os.getenv("STATUS_TOKEN")
repo = os.getenv("GITHUB_REPOSITORY") # hafizecim/YDS-Word-A-Day

if token and repo:
    url = f"https://api.github.com/repos/{repo}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"description": repo_description}
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Depo açıklaması başarıyla güncellendi!")
    else:
        print(f"Hata oluştu: {response.status_code}, {response.text}")
