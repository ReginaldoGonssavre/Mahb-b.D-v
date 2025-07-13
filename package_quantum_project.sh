#!/bin/bash

# Nome da pasta do projeto
PROJETO_ORIGINAL="$HOME/Quantum X2"

# Nome do arquivo zip final
NOME_ZIP="RAVIQUANTIC_OS_REDES_NEURAIS_QUANTICAS_project.zip"

# Caminho de destino final no Android
CAMINHO_DESTINO="/storage/emulated/0/Download"

# Acessa a pasta do projeto
cd "$PROJETO_ORIGINAL" || { echo "❌ Pasta não encontrada!"; exit 1; }

# Compacta apenas o conteúdo da pasta (sem incluir o nome da pasta)
echo "🔧 Compactando conteúdo da pasta $PROJETO_ORIGINAL..."
zip -r "$HOME/$NOME_ZIP" ./*

# Move o arquivo zip para Downloads
echo "🚚 Movendo para $CAMINHO_DESTINO..."
mv "$HOME/$NOME_ZIP" "$CAMINHO_DESTINO/"

# Mensagem final
echo "✅ Backup completo!"
echo "📂 Salvo em: $CAMINHO_DESTINO/$NOME_ZIP"#!/bin/bash

# Nome do projeto original
PROJETO_ORIGINAL="$HOME/Quantum X2"

# Nome do zip final
NOME_ZIP="RAVIQUANTIC_OS_REDES_NEURAIS_QUANTICAS_project.zip"

# Caminho de saída final
CAMINHO_DESTINO="/storage/emulated/0/Download"

# Cria o .zip na home
echo "🔧 Compactando projeto..."
zip -r "$HOME/$NOME_ZIP" "$PROJETO_ORIGINAL"

# Move para a pasta Downloads do Android
echo "🚚 Movendo para $CAMINHO_DESTINO..."
mv "$HOME/$NOME_ZIP" "$CAMINHO_DESTINO/"

# Mensagem final
echo "✅ Backup concluído!"
echo "➡️ Arquivo salvo em: $CAMINHO_DESTINO/$NOME_ZIP"#!/bin/bash
echo "Empacotando o projeto Quantum_NovaOS_2025..."
# Navega para o diretório home para garantir que o zip seja criado lá
cd /data/data/com.termux/files/home/
# Cria um arquivo zip de todo o diretório do projeto
zip -r RAVIQUANTIC_OS_REDES_NEURAIS_QUANTICAS_project.zip quantum_internet_simulation/
echo "Projeto empacotado com sucesso em: /data/data/com.termux/files/home/RAVIQUANTIC_OS_REDES_NEURAIS_QUANTICAS_project.zip"
echo "Você pode agora transferir este arquivo para outro desenvolvedor."
