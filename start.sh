#!/bin/bash
termux-wake-lock

# Sessão 1: Backend
termux-new-session -d -s backend "cd ~/quantum-agent-app/backend && uvicorn main:app --host 0.0.0.0 --port 8000"

# Sessão 2: Frontend
termux-new-session -d -s frontend "cd ~/quantum-agent-app/frontend && npm run build && npx cap sync"

# Manter o Termux ativo
sleep infinity

