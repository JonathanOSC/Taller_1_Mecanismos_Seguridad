import re, math, pandas as pd
from score_request import is_anomalous, score

def shannon_entropy(s):
    if not s: return 0.0
    probs = [s.count(c) / len(s) for c in set(s)]
    return -sum(pr * math.log2(pr) for pr in probs)

SUSPICIOUS = re.compile(r"(--|;|<script|\.\./|\bUNION\b|\bOR\b|\s+1=1)", re.I)

def extract(url, body='', req_per_minute=10):
    return {
        'url_length': len(url), 'body_length': len(body),
        'entropy': shannon_entropy(url + body),
        'n_params': url.count('&') + 1 if '?' in url else 0,
        'has_suspicious_chars': bool(SUSPICIOUS.search(url + body)),
        'req_per_minute': req_per_minute
    }

peticiones = [
    # --- 5 NORMALES ---
    {"tipo": "Normal", "url": "/rest/products/search?q=apple", "rpm": 12},
    {"tipo": "Normal", "url": "/rest/user/login", "rpm": 5},
    {"tipo": "Normal", "url": "/api/BasketItems", "rpm": 20},
    {"tipo": "Normal", "url": "/rest/products/search?q=banana", "rpm": 8},
    {"tipo": "Normal", "url": "/assets/public/favicon.ico", "rpm": 15},

    # --- 5 ATAQUES/ANOMALÍAS ---
    {"tipo": "Ataque (SQLi HPP Fase 2)", "url": "/rest/products/search?q=a%27%20UNION&q=SELECT%20*%20FROM%20users--", "rpm": 10},
    {"tipo": "Ataque (XSS)", "url": "/rest/products/search?q=<script>alert(1)</script>", "rpm": 10},
    {"tipo": "Ataque (SQLi URL Encoded)", "url": "/rest/products/search?q=%27%20OR%20%271%27%3D%271", "rpm": 10},
    {"tipo": "Ataque (Path Traversal)", "url": "/public/images/../../../../etc/passwd", "rpm": 10},
    {"tipo": "Anomalía (Bot Ráfaga)", "url": "/rest/products/search?q=apple", "rpm": 250} # req_per_minute altísimo
]

print(f"{'Tipo':<28} | {'Score':<8} | {'Bloqueado'}")
print("-" * 55)
for p in peticiones:
    datos = extract(p["url"], req_per_minute=p["rpm"])
    puntaje = score(datos)
    bloqueado = is_anomalous(datos)
    print(f"{p['tipo']:<28} | {puntaje:>8.4f} | {bloqueado}")
