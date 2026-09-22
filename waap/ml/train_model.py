import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

# Leer el dataset de tráfico normal
df = pd.read_csv('logs/features_normal_traffic.csv')

# Seleccionar las columnas para el modelo
X = df[['url_length', 'body_length', 'entropy', 'n_params', 'has_suspicious_chars', 'req_per_minute']].astype(float)

# Estandarizar los datos
scaler = StandardScaler().fit(X)
X_scaled = scaler.transform(X)

# Entrenar el modelo Isolation Forest
model = IsolationForest(
    n_estimators=200, contamination=0.02, random_state=42
).fit(X_scaled)

# Guardar el modelo entrenado y el scaler
joblib.dump({'model': model, 'scaler': scaler}, 'waap/ml/model.pkl')
print('Modelo entrenado y guardado en waap/ml/model.pkl')
