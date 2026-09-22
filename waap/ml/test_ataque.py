from score_request import is_anomalous, score

# Tu ataque SQLi fragmentado
peticion_ataque = {
    'url_length': 85,
    'body_length': 0,
    'entropy': 4.8, 
    'n_params': 2,
    'has_suspicious_chars': True,
    'req_per_minute': 10
}

# Tu ataque Bot (Ráfaga)
peticion_bot = {
    'url_length': 30,
    'body_length': 0,
    'entropy': 2.1,
    'n_params': 0,
    'has_suspicious_chars': False,
    'req_per_minute': 150 
}

print("--- Resultados IA/ML ---")
print(f"SQLi Fragmentado -> Score: {score(peticion_ataque):.4f} | Bloquear: {is_anomalous(peticion_ataque)}")
print(f"Ráfaga (Bot)     -> Score: {score(peticion_bot):.4f} | Bloquear: {is_anomalous(peticion_bot)}")
