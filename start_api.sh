#!/bin/bash
# Script de inicialização da API Simulador Jogo Imobiliário
# Porta: 8080

echo "=========================================="
echo "🎮 API Simulador de Jogo Imobiliário"
echo "=========================================="
echo ""

# Definir diretório do projeto
PROJECT_DIR="/system"

# Navegar para o diretório
cd "$PROJECT_DIR" || exit 1

# Ativar ambiente virtual
echo "📦 Ativando ambiente virtual..."
source venv/bin/activate

# Verificar se as dependências estão instaladas
echo "🔍 Verificando dependências..."
pip list | grep -q fastapi || {
    echo "⚠️  Dependências não encontradas. Instalando..."
    pip install -r requirements.txt --quiet
}

# Iniciar API
echo ""
echo "🚀 Iniciando API na porta 8080..."
echo "📖 Documentação: http://localhost:8080/docs"
echo "🔗 API: http://localhost:8080/jogo/simular"
echo ""
echo "Pressione CTRL+C para parar"
echo "=========================================="
echo ""

# Executar API
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload

