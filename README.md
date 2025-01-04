# EAGI Processor para Asterisk

Procesador EAGI (Enhanced Asterisk Gateway Interface) con reconocimiento de voz en tiempo real para Asterisk PBX.

## Características

- Procesamiento de audio en tiempo real
- Reconocimiento de voz usando Google Speech Recognition
- Soporte para español
- Fácil integración con Asterisk

## Requisitos Previos

- Python 3.6 o superior
- Asterisk PBX instalado y configurado
- Conexión a Internet (para el reconocimiento de voz)
- Paquetes del sistema: `portaudio19-dev` y `python3-dev`

## Instalación

1. Instalar las dependencias del sistema:
```bash
sudo apt-get install portaudio19-dev python3-dev


## dialplan de Asterisk añadiendo

exten => XXX,1,Answer()
exten => XXX,n,EAGI(/usr/local/bin/eagi-processor)
exten => XXX,n,Hangup()

## Reinicia Asterisk

sudo systemctl restart asterisk