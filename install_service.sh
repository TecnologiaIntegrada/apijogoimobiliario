#!/bin/bash
# Script para instalar o serviço systemd

echo "==========================================================="
echo "Instalando como serviço em systemd para plataformas linux  "
echo "==========================================================="

# Copiar arquivo de serviço
echo "📋 Copiando arquivo de serviço..."
sudo cp /system/api-simulator.service /etc/systemd/system/

# Recarregar systemd
echo "🔄 Recarregando systemd..."
sudo systemctl daemon-reload

# Habilitar serviço
echo "✅ Habilitando serviço..."
sudo systemctl enable api-simulator.service

echo ""
echo "=========================================="
echo "✅ Serviço instalado com sucesso!"
echo "=========================================="
echo ""
echo "Comandos úteis:"
echo "  Iniciar:  sudo systemctl start api-simulator"
echo "  Parar:    sudo systemctl stop api-simulator"
echo "  Status:   sudo systemctl status api-simulator"
echo "  Logs:     sudo journalctl -u api-simulator -f"
echo ""
echo "A API iniciará automaticamente ao reiniciar o servidor"
echo "=========================================="

