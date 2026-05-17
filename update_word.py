import json
import random
from datetime import datetime

# 1. Kelime havuzunu oku
with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

# Rastgele bir kelime seç
selected = random.choice(words)
today = datetime.now().strftime('%Y-%m-%d')

# 2. Deponun Ana README dosyasını güncelle (Kutuda görünecek kısım burası!)
readme_content = f"""# 🎯 Günün Kelimesi: {selected['word']} ({selected['meaning']})

---

### 📝 Kelime Detayları ({today})
* **Kelime:** {selected['word']}
* **Anlamı:** {selected['meaning']}
* **Örnek Cümle:** *{selected['example']}*

---
*Bu depo her gün otomatik olarak yeni bir YDS kelimesi ile güncellenmektedir.*
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("README.md başarıyla güncellendi!")
