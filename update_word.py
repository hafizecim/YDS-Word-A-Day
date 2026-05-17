import json
import random
from datetime import datetime

# 1. Kelime havuzunu oku
with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

# Rastgele bir kelime seç
selected = random.choice(words)
today = datetime.now().strftime('%Y-%m-%d')

word = selected['word']
meaning = selected['meaning']

# Profilinde kutu gibi görünecek şık bir SVG resmi oluşturuyoruz
svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="450" height="80" viewBox="0 0 450 80">
    <rect width="448" height="78" x="1" y="1" rx="10" fill="#0d1117" stroke="#30363d" stroke-width="2"/>
    <text x="20" y="35" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="16" font-weight="bold" fill="#58a6ff">🎯 YDS Today:</text>
    <text x="125" y="35" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="16" font-weight="bold" fill="#ffffff">{word}</text>
    <text x="20" y="60" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="14" fill="#8b949e">Anlamı: {meaning}</text>
</svg>"""

# SVG dosyasını kaydet
with open('yds_word.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print("SVG Görseli başarıyla oluşturuldu!")
