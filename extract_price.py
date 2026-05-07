"""
Запустите один раз: python extract_price.py
Извлекает прайс из calculator.html → сохраняет в price_data.json
"""
import json, re, sys
from pathlib import Path

html_path = Path(__file__).parent.parent / "calculator.html"
out_path  = Path(__file__).parent / "price_data.json"

if not html_path.exists():
    sys.exit(f"Файл не найден: {html_path}")

content = html_path.read_text(encoding="utf-8")
m = re.search(r"const EMBEDDED\s*=\s*(\{.+?\});\s*\n//", content, re.DOTALL)
if not m:
    sys.exit("Не удалось найти EMBEDDED в HTML")

data = json.loads(m.group(1))
out_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
print(f"✅ Извлечено {len(data)} механизмов → {out_path}")
