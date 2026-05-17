import json
import random
from datetime import datetime
import os

# 1. Kelime havuzunu oku (Tek Kaynak)
with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

# Rastgele tek bir kelime seç (Senkronizasyon sorunu bitti!)
selected = random.choice(words)
today = datetime.now().strftime('%Y-%m-%d')
word = selected['word'].strip() # Boşlukları temizle
meaning = selected['meaning'].strip()
example = selected['example'].strip()

print(f"Secilen Kelime: {word}, Anlami: {meaning}")

# 2. Daha Şık Tasarım: Yuvarlatılmış Gradient Kutu
# Renkler: #0d1117 (Siyah), #161b22 (Füme), #58a6ff (Mavi), #ffffff (Beyaz)
svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="450" height="90" viewBox="0 0 450 90">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d1117;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#161b22;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <rect width="448" height="88" x="1" y="1" rx="15" fill="url(#grad1)" stroke="#30363d" stroke-width="2"/>
  
  <rect width="8" height="50" x="15" y="20" rx="4" fill="#58a6ff" />

  <text x="35" y="38" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="16" font-weight="bold" fill="#58a6ff">
    🎯 YDS TODAY:
  </text>
  
  <text x="160" y="38" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="18" font-weight="bold" fill="#ffffff" font-style="italic">
    {word}
  </text>
  
  <text x="35" y="65" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="14" fill="#8b949e">
    Anlamı: {meaning}
  </text>
</svg>"""

# SVG dosyasını kaydet
with open('yds_word.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

# 3. README dosyasını da aynı kelime ile baştan oluştur (Senkronizasyon garantisi!)
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

print("Hem SVG hem README başarıyla güncellendi!")
