import sys

def log(message):
    """Escribe mensajes de log en stderr."""
    sys.stderr.write(message + "\n")
    sys.stderr.flush()

def read_agi_env():
    """Lee variables de entorno AGI."""
    agi_env = {}
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        key, value = line.split(": ", 1)
        agi_env[key] = value
    return agi_env
