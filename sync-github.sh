#!/bin/bash

# CONFIGURAÇÕES
REPO_URL="https://github.com/ReginaldoGonssavre/Mahb-b.D-v.git"
BRANCH="main"
PASTA_LOCAL="$HOME"  # Altere se sua pasta for diferente

# Acessar a pasta local
cd "$PASTA_LOCAL" || exit 1

# Inicializar git se ainda não estiver inicializado
if [ ! -d ".git" ]; then
  git init
  git remote add origin "$REPO_URL"
  git checkout -b "$BRANCH"
else
  git checkout "$BRANCH"
fi

# Sincronizar arquivos
git add .
git commit -m "Sync automático $(date +'%Y-%m-%d %H:%M:%S')" || true
git push origin "$BRANCH"
