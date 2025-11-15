# .github/scripts/generate_readme.py
import requests
from datetime import datetime
import pytz
import os


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(REPO_ROOT, 'README.md')
ASSETS_DIR = os.path.join(REPO_ROOT, 'assets')
SVG_PATH = os.path.join(ASSETS_DIR, 'animated.svg')


os.makedirs(ASSETS_DIR, exist_ok=True)


# 1) get a random quote
try:
r = requests.get('https://api.quotable.io/random', timeout=10)
data = r.json()
quote = f"{data.get('content')} — {data.get('author')}"
except Exception:
quote = "Be yourself; everyone else is already taken. — Oscar Wilde"


# 2) timestamp
tz = pytz.timezone('Asia/Kolkata')
now = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z')


# 3) update README placeholders
with open(README, 'r', encoding='utf-8') as f:
content = f.read()


content = content.replace('<!--LAST_UPDATED-->', now)
content = content.replace('<!--RANDOM_QUOTE-->', quote)


with open(README, 'w', encoding='utf-8') as f:
f.write(content)


# 4) generate a tiny animated SVG (a moving circle)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="120" viewBox="0 0 600 120">
<rect width="100%" height="100%" fill="transparent" />
<g>
<circle cx="60" cy="60" r="20">
<animate attributeName="cx" from="60" to="540" dur="4s" repeatCount="indefinite" />
<animate attributeName="fill" values="#FF7A7A;#7AD3FF;#9AFF7A;#FFDD7A;#FF7A7A" dur="8s" repeatCount="indefinite" />
</circle>
</g>
</svg>'''


with open(SVG_PATH, 'w', encoding='utf-8') as f:
f.write(svg)


print('Generated README and SVG successfully')
