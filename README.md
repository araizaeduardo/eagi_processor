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

### 1. Clonar el Repositorio

```bash
git clone https://github.com/araizaeduardo/eagi_processor.git
cd eagi_processor
```

### 2. Instalar Dependencias del Sistema

```bash
sudo apt-get update
sudo apt-get install -y portaudio19-dev python3-dev python3-pip
```

### 3. Instalar el Módulo

Tienes dos opciones para instalar el módulo:

#### Opción A: Usando el Script de Instalación (Recomendado)
```bash
chmod +x install.sh
./install.sh
```

#### Opción B: Instalación Manual
```bash
pip3 install .
SCRIPT_PATH=$(which eagi-processor)
sudo ln -sf $SCRIPT_PATH /usr/local/bin/eagi-processor
sudo chmod +x /usr/local/bin/eagi-processor
```

## Configuración de Asterisk

### 1. Configurar el Dialplan

Edita tu archivo de configuración del dialplan (usualmente en `/etc/asterisk/extensions.conf`):

```bash
sudo nano /etc/asterisk/extensions.conf
```

### 2. Añade la Configuración EAGI

Agrega las siguientes líneas en el contexto deseado:

```asterisk
exten => XXX,1,Answer()
exten => XXX,n,EAGI(/usr/local/bin/eagi-processor)
exten => XXX,n,Hangup()
```

Reemplaza `XXX` con el número de extensión que desees usar.

### 3. Reiniciar Asterisk

```bash
sudo systemctl restart asterisk
```

## Verificación de la Instalación

1. Verifica que el script esté instalado:
```bash
which eagi-processor
```

2. Verifica los permisos:
```bash
ls -l /usr/local/bin/eagi-processor
```

3. Monitorea los logs durante una llamada:
```bash
tail -f /var/log/asterisk/messages
```

## Solución de Problemas

Si encuentras algún problema, verifica:

1. Que el script tenga permisos de ejecución:
```bash
sudo chmod +x /usr/local/bin/eagi-processor
```

2. Que Asterisk tenga permisos para ejecutar el script:
```bash
sudo chown asterisk:asterisk /usr/local/bin/eagi-processor
```

3. Que las dependencias estén instaladas correctamente:
```bash
pip3 list | grep "speech"
```

## Soporte

Para reportar problemas o solicitar ayuda, por favor crea un issue en:
https://github.com/araizaeduardo/eagi_processor/issues