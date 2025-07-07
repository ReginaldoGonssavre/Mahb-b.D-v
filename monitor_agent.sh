#!/bin/bash
export PYTHONUNBUFFERED=1
RESTART_COUNT=0
MAX_RESTARTS=50

while [ $RESTART_COUNT -lt $MAX_RESTARTS ]; do
    echo "▶ Iniciando agente (tentativa #$((RESTART_COUNT+1)))"
    streamlit run app.py --server.headless true --server.runOnSave true
    
    EXIT_CODE=$?
    echo "⚠ Agente finalizado com código $EXIT_CODE"
    
    if [ $EXIT_CODE -eq 0 ]; then
        echo "✅ Desligamento normal"
        break
    else
        ((RESTART_COUNT++))
        echo "🔄 Reiniciando em 3 segundos..."
        sleep 3
    fi
done

echo "⛔ Máximo de reinícios atingido"
