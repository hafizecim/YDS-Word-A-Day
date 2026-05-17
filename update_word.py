import json
import random
from datetime import datetime
import os
import requests

# 1. Kelime havuzunu oku
with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

# Rastgele bir kelime seç
selected = random.choice(words)
today = datetime.now().strftime('%Y-%m-%d')

# Depo açıklaması için şık format
repo_description = f"🎯 {selected['word']}: {selected['meaning']}"

# 2. Gunun_Kelimesi.md dosyasını güncelle
with open('Gunun_Kelimesi.md', 'w', encoding='utf-8') as f:
    f.write(f"# 📝 Günün YDS Kelimesi ({today})\n\n## 🎯 **{selected['word']}**\n* **Anlamı:** {selected['meaning']}\n* **Örnek Cümle:** *{selected['example']}*")

# 3. GitHub API ile Depo Açıklamasını Güncelle
# Burayı daha garanti bir yönteme çevirdik:
token = os.getenv("STATUS_TOKEN")
repo = os.getenv("GITHUB_REPOSITORY") # hafizecim/YDS-Word-A-Day

if not token:
    print("HATA: STATUS_TOKEN bulunamadı! Depo ayarlarından Secrets kısmını kontrol edin.")
else:
    url = f"https://api.github.com/repos/{repo}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"description": repo_description}
    
    response = requests.patch(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print(f"BAŞARILI: Depo açıklaması '{repo_description}' olarak değiştirildi!")
    else:
        print(f"API HATASI! Durum Kodu: {response.status_code}")
        print(f"Hata Mesajı: {response.text}")
