
"""
Exemplo de detecção de anomalias com ML para eventos AIOps, integrado com Neptune.ai.
Pode ser expandido para pipelines quânticos e workloads complexos.
"""

import numpy as np
from sklearn.ensemble import IsolationForest
import neptune
import os

# --- Integração com Neptune.ai ---
# IMPORTANTE: Configure as variáveis de ambiente NEPTUNE_PROJECT e NEPTUNE_API_TOKEN
#
# Para mais detalhes: https://docs.neptune.ai/setup/setting_credentials/
run = neptune.init_run(
    name="anomaly-detection-experiment",
    description="Experimento de detecção de anomalias com IsolationForest.",
    tags=["aiops", "isolation-forest", "poc"]
)

# Parâmetros do modelo
params = {"contamination": 0.05}
run["parameters"] = params

# Simula métricas coletadas
metrics = np.random.normal(loc=0, scale=1, size=(100, 3))
anomaly_metrics = np.random.normal(loc=5, scale=1, size=(5, 3))
all_metrics = np.vstack([metrics, anomaly_metrics])

# Treinamento do modelo
model = IsolationForest(contamination=params["contamination"])
model.fit(all_metrics)
preds = model.predict(all_metrics)

# Logando resultados no Neptune
run["results/predictions"] = preds

print("Resultados do modelo:")
for idx, pred in enumerate(preds):
    if pred == -1:
        anomaly_info = f"Anomalia detectada na métrica {idx}: {all_metrics[idx]}"
        print(anomaly_info)
        # Loga cada anomalia encontrada
        run[f"results/anomalies/anomaly_{idx}"].log(str(all_metrics[idx]))

# Finaliza a execução do Neptune
run.stop()

print("\nExperimento registrado com sucesso no Neptune.ai!")
print("Acesse o link no terminal para visualizar os resultados.")
