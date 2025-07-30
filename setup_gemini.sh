#!/bin/bash

echo "🔧 Iniciando configuração do ambiente para Gemini CLI..."

# 🔑 Chave do Gemini
export GEMINI_API_KEY="COLE_SUA_CHAVE_GEMINI_AQUI"
echo "✅ GEMINI_API_KEY configurada."

# 🌐 Supabase
export SUPABASE_URL="https://zsuuikxrulddbfugiomw.supabase.co"
export SUPABASE_KEY="COLE_SUA_SUPABASE_KEY_AQUI"
echo "✅ SUPABASE_URL e SUPABASE_KEY configuradas."

# 🌲 Pinecone
export PINECONE_API_KEY="COLE_SUA_CHAVE_PINECONE"
export PINECONE_ENVIRONMENT="COLE_SEU_AMBIENTE_PINECONE"
export PINECONE_INDEX_NAME="COLE_SEU_INDEX_PINECONE"
echo "✅ PINECONE_API_KEY, ENVIRONMENT e INDEX configurados."

# ✅ Diagnóstico final
echo ""
echo "📡 Variáveis carregadas nesta sessão:"
env | grep -E 'GEMINI_API_KEY|SUPABASE|PINECONE'

echo ""
echo "🎯 Agora você pode rodar: gemini"
echo "💡 Lembre-se: ao reiniciar o Termux, este ambiente será perdido."
