import time
import logging
from flask import Flask
from rasp_agent import build_login_query

# Configurar logging para ver la advertencia del RASP
logging.basicConfig(level=logging.WARNING)
app = Flask(__name__)

# Necesitamos simular el contexto de una petición web para que funcione el abort(403)
with app.test_request_context():
    print("\n--- CASO DE PRUEBA 1: Tráfico Normal ---")
    try:
        consulta = build_login_query("admin", "password123")
        print(f"Consulta generada con éxito: {consulta}")
    except Exception as e:
        print(f"Error: {e}")

    print("\n--- CASO DE PRUEBA 2: Ataque de Evasión (Fase 2) ---")
    try:
        # Simulamos que los parámetros fragmentados ya llegaron a la base de datos
        payload_malicioso = "a' UNION SELECT * FROM users--"
        consulta = build_login_query("admin", payload_malicioso)
        print(f"Consulta generada con éxito: {consulta}")
    except Exception as e:
        print(f"¡ÉXITO DEL LABORATORIO! La aplicación detuvo la ejecución: {e}")

    print("\n--- PRUEBA DE LATENCIA (10,000 iteraciones) ---")
    # Función gemela SIN el decorador RASP para comparar
    def build_login_query_sin_rasp(username, password):
        return f"SELECT * FROM users WHERE user='{username}' AND pass='{password}'"

    # Medir tiempo SIN RASP
    inicio_sin = time.time()
    for _ in range(10000):
        build_login_query_sin_rasp("usuario", "clave")
    tiempo_sin = (time.time() - inicio_sin) * 1000

    # Medir tiempo CON RASP
    inicio_con = time.time()
    for _ in range(10000):
        build_login_query("usuario", "clave")
    tiempo_con = (time.time() - inicio_con) * 1000

    print(f"Tiempo SIN RASP: {tiempo_sin:.2f} ms")
    print(f"Tiempo CON RASP: {tiempo_con:.2f} ms")
    print(f"Impacto por inspección (Overhead): {tiempo_con - tiempo_sin:.2f} ms")
