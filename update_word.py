import json
import random
from datetime import datetime

# 1. Kelime havuzunu oku
with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

# Rastgele bir kelime seç
selected = random.choice(words)
today = datetime.now().strftime('%Y-%m-%d')

# 2. Gunun_Kelimesi.md dosyasını güncelle
with open('Gunun_Kelimesi.md', 'w', encoding='utf-8') as f:
    f.write(f"# 📝 Günün YDS Kelimesi ({today})\n\n## 🎯 **{selected['word']}**\n* **Anlamı:** {selected['meaning']}\n* **Örnek Cümle:** *{selected['example']}*")

# 3. GitHub workflow'un okuyabilmesi için kelimeyi düz metin olarak dışarı yaz
repo_description = f"🎯 {selected['word']}: {selected['meaning']}"
with open('repo_desc.txt', 'w', encoding='utf-8') as f:
    f.write(repo_description)

print("Kelime başarıyla seçildi ve dosyaya yazıldı.")
