#!/data/data/com.termux/files/usr/bin/bash

echo "🚀 RAVIAN QUANTUM - Deploy Script"
echo "================================"

# Build do projeto
echo "📦 Building RAVIAN QUANTUM..."
npm run build

# Commit e push
echo "📤 Uploading to GitHub..."
git add .
git commit -m "🔄 RAVIAN QUANTUM update - $(date)"
git push origin main

echo "✅ RAVIAN QUANTUM deployed successfully!"
echo "🌐 GitHub: https://github.com/SEU_USUARIO/ravian-quantum"
