#!/usr/bin/env python3
import sys
import os
import wave
import speech_recognition as sr
from io import BytesIO
from eagi_processor.utils import log, read_agi_env

def process_audio_chunk(recognizer, audio_data):
    """Procesa un chunk de audio usando reconocimiento de voz."""
    try:
        # Convertir el audio raw a un formato que speech_recognition pueda usar
        text = recognizer.recognize_google(audio_data, language="es-ES")
        log(f"Texto reconocido: {text}")
        return text
    except sr.UnknownValueError:
        log("No se pudo entender el audio")
        return None
    except sr.RequestError as e:
        log(f"Error en el servicio de reconocimiento de voz: {e}")
        return None

def main():
    """Punto de entrada del script EAGI."""
    # Leer variables de entorno AGI
    agi_env = read_agi_env()
    log("Variables AGI recibidas:")
    for key, value in agi_env.items():
        log(f"{key}: {value}")

    # Inicializar el reconocedor de voz
    recognizer = sr.Recognizer()
    audio_buffer = BytesIO()
    
    # Leer el audio en tiempo real
    with open("/dev/fd/3", "rb") as audio_stream:
        chunk_size = 1024 * 8  # 8KB chunks
        audio_data = audio_stream.read(chunk_size)
        
        while audio_data:
            audio_buffer.write(audio_data)
            
            # Procesar cuando tengamos suficientes datos
            if audio_buffer.tell() >= chunk_size * 10:  # Procesar cada ~80KB
                audio_buffer.seek(0)
                try:
                    # Convertir el audio raw a un formato compatible con speech_recognition
                    audio = sr.AudioData(audio_buffer.read(), 
                                       sample_rate=8000,  # Asterisk típicamente usa 8kHz
                                       sample_width=2)    # 16-bit audio
                    process_audio_chunk(recognizer, audio)
                except Exception as e:
                    log(f"Error procesando audio: {e}")
                
                # Limpiar buffer para el siguiente chunk
                audio_buffer = BytesIO()
            
            audio_data = audio_stream.read(chunk_size)

    log("Procesamiento de audio finalizado.")

if __name__ == "__main__":
    main()
