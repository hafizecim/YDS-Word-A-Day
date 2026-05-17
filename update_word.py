import json
import random
from datetime import datetime

# Kelime havuzunu oku
with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

# Rastgele bir kelime seç
selected = random.choice(words)

# Bugünün tarihini al
today = datetime.now().strftime('%Y-%m-%d')

# Yazdırılacak Markdown içeriğini hazırla
content = f"""# 📝 Günün YDS Kelimesi ({today})

## 🎯 **{selected['word']}**
* **Anlamı:** {selected['meaning']}
* **Örnek Cümle:** *{selected['example']}*

---
*Bu dosya GitHub Actions botu tarafından otomatik olarak güncellenmiştir. YDS yolculuğunda başarılar!*
"""

# Dosyayı kaydet
with open('Gunun_Kelimesi.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Bugünün kelimesi başarıyla güncellendi: {selected['word']}")
