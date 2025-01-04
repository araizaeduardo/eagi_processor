#!/bin/bash

# Colores para mensajes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}Instalando EAGI Processor para Asterisk...${NC}"

# Instalar dependencias del sistema
echo -e "${BLUE}Instalando dependencias del sistema...${NC}"
sudo apt-get update
sudo apt-get install -y portaudio19-dev python3-dev python3-pip

# Instalar el módulo Python
echo -e "${BLUE}Instalando módulo Python...${NC}"
pip3 install .

# Crear enlace simbólico al script
echo -e "${BLUE}Configurando script EAGI...${NC}"
SCRIPT_PATH=$(which eagi-processor)
sudo ln -sf $SCRIPT_PATH /usr/local/bin/eagi-processor
sudo chmod +x /usr/local/bin/eagi-processor

echo -e "${GREEN}Instalación completada!${NC}"
echo -e "${BLUE}Para usar el script, añade la siguiente línea en tu dialplan de Asterisk:${NC}"
echo "exten => XXX,n,EAGI(/usr/local/bin/eagi-processor)"

[tu-contexto]
exten => XXX,1,Answer()
exten => XXX,n,EAGI(/usr/local/bin/eagi-processor)
exten => XXX,n,Hangup()

tail -f /var/log/asterisk/messages
