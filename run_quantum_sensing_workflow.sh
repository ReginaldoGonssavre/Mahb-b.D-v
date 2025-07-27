#!/bin/bash

# --- Configurações --- #

# Parâmetros da simulação
SENSOR_MODEL="NV_Center"
TARGET="material_defects"
SENSITIVITY="ultra_high"
FREQUENCY_RANGE="0.1GHz-10GHz"
SIMULATION_OUTPUT_FILE="./results/simulation_output.json"

# Parâmetros de integração com middleware
PROTOCOL="Q-Sync"
MODE="real-time"
OUTPUT_FIRMWARE_FILE="./firmware/q_sensor_v1.0.hex"

# Parâmetros de monitoramento com IA
AI_MODEL="quantumAI_v2"
DEPLOY_MODE="edge-device"
ALERTS="on"

# URL da API de dados industriais
INDUSTRIAL_API_URL="https://api.industria4.0.br/upload"

# Nome do ambiente virtual
VENV_NAME="quantum_sensing_env"

# Repositório do SDK de sensoriamento quântico
QUANTUM_SENSING_SDK_REPO="https://github.com/QuantumLabOrg/quantum-sensing-sdk.git"
QUANTUM_SENSING_SDK_DIR="quantum-sensing-sdk"

# --- Funções Auxiliares --- #

log_step() {
  echo "\n--- $1 ---"
}

handle_error() {
  echo "\n!!! ERRO: $1 !!!\n"
  exit 1
}

# --- Fluxo de Trabalho --- #

log_step "1. Configurando ambiente virtual de desenvolvimento quântico"
if [ -d "$VENV_NAME" ]; then
  echo "Ambiente virtual '$VENV_NAME' já existe. Ativando..."
  source "$VENV_NAME/bin/activate" || handle_error "Falha ao ativar ambiente virtual existente."
else
  echo "Criando e ativando ambiente virtual '$VENV_NAME'..."
  python3 -m venv "$VENV_NAME" || handle_error "Falha ao criar ambiente virtual."
  source "$VENV_NAME/bin/activate" || handle_error "Falha ao ativar ambiente virtual recém-criado."
fi

log_step "2. Clonando repositório de sensores quânticos"
if [ -d "$QUANTUM_SENSING_SDK_DIR" ]; then
  echo "Repositório '$QUANTUM_SENSING_SDK_DIR' já existe. Pulando clone e navegando para o diretório..."
  cd "$QUANTUM_SENSING_SDK_DIR" || handle_error "Falha ao navegar para o diretório do SDK."
  git pull || echo "Aviso: Falha ao atualizar o repositório do SDK. Continuando..."
else
  echo "Clonando repositório '$QUANTUM_SENSING_SDK_REPO'...
  if ! git clone "$QUANTUM_SENSING_SDK_REPO"; then
    echo "Aviso: Falha ao clonar o repositório. Criando diretório dummy e requirements.txt para continuar."
    mkdir -p "$QUANTUM_SENSING_SDK_DIR" || handle_error "Falha ao criar diretório dummy."
    echo "qiskit
numpy
scipy" > "$QUANTUM_SENSING_SDK_DIR/requirements.txt" # Create a dummy requirements.txt
  fi
  cd "$QUANTUM_SENSING_SDK_DIR" || handle_error "Falha ao navegar para o diretório do SDK."
fi

log_step "3. Instalando dependências essenciais"
if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt || handle_error "Falha ao instalar dependências do requirements.txt."
else
  handle_error "Arquivo 'requirements.txt' não encontrado no diretório do SDK. Não é possível instalar dependências."
fi

log_step "4. Executando simulação inicial de sensores quânticos"
mkdir -p "$(dirname "$SIMULATION_OUTPUT_FILE")" || handle_error "Falha ao criar diretório para saída da simulação."
python run_simulation.py --sensor-model="$SENSOR_MODEL" --target="$TARGET" \
  --sensitivity="$SENSITIVITY" --frequency-range="$FREQUENCY_RANGE" --output="$SIMULATION_OUTPUT_FILE" \
  || handle_error "Falha ao executar a simulação do sensor quântico."

log_step "5. Integrando com middleware de software embarcado"
mkdir -p "$(dirname "$OUTPUT_FIRMWARE_FILE")" || handle_error "Falha ao criar diretório para saída do firmware."
python integrate_middleware.py --protocol="$PROTOCOL" --mode="$MODE" \
  --output-firmware="$OUTPUT_FIRMWARE_FILE" || handle_error "Falha ao integrar com middleware embarcado."

log_step "6. Configurando monitoramento com inteligência artificial"
python ai_monitor.py --input="$SIMULATION_OUTPUT_FILE" --model="$AI_MODEL" \
  --deploy-mode="$DEPLOY_MODE" --alerts="$ALERTS" || handle_error "Falha ao configurar monitoramento com IA."

log_step "7. Exportando logs e relatórios para API de dados industriais"
if [ -f "$SIMULATION_OUTPUT_FILE" ]; then
  curl -X POST "$INDUSTRIAL_API_URL" \
    -H "Content-Type: application/json" \
    -d @"$SIMULATION_OUTPUT_FILE" || handle_error "Falha ao exportar dados para a API industrial."
else
  handle_error "Arquivo de saída da simulação ($SIMULATION_OUTPUT_FILE) não encontrado para exportação."
fi

log_step "Fluxo de trabalho de sensoriamento quântico concluído com sucesso!"

# Desativar ambiente virtual (opcional, dependendo do uso posterior)
deactivate
