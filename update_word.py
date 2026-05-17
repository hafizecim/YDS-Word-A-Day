import json
import random
from datetime import datetime

# 1. Kelime havuzunu oku (Tek bir kelime seçiyoruz, uyuşmazlık bitiyor)
with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

selected = random.choice(words)
today = datetime.now().strftime('%Y-%m-%d')
word = selected['word'].strip()
meaning = selected['meaning'].strip()
example = selected['example'].strip()

print(f"Bugünün Kelimesi: {word}")

# 2. Sevdiğin Siyah Kutunun Süslenmiş ve Ortalı Versiyonu (SVG)
# Kelimeyi tam ortalamak için text-anchor="middle" kullandım, bitişiklik çözüldü!
svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="550" height="100" viewBox="0 0 550 100">
  <rect width="546" height="96" x="2" y="2" rx="12" fill="#0d1117" stroke="#30363d" stroke-width="2"/>
  
  <rect width="534" height="84" x="8" y="8" rx="8" fill="none" stroke="#238636" stroke-width="1" stroke-dasharray="4,4"/>

  <text x="275" y="38" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="15" font-weight="bold" fill="#58a6ff" text-anchor="middle" letter-spacing="1.5">
    🎯 YDS TODAY
  </text>
  
  <text x="275" y="68" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="20" font-weight="bold" fill="#ffffff" text-anchor="middle">
    {word} <tspan fill="#8b949e" font-size="15" font-weight="normal"> ({meaning})</tspan>
  </text>
</svg>"""

# SVG'yi kaydet
with open('yds_word.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

# 3. README dosyasını da aynı kelimeyle eşitleyerek baştan yaz
readme_content = f"""# 🎯 Günün Kelimesi: **{word}** ({meaning})

---

### 📝 Kelime Detayları ({today})
* **Kelime:** **{word}**
* **Anlamı:** {meaning}
* **Örnek Cümle:** *{example}*

---
*Bu depo her gün otomatik olarak yeni bir YDS kelimesi ile güncellenmektedir.*
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("Süslü siyah kutu ve README başarıyla eşitlendi!")
