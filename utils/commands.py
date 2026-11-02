# utils/commands.py
import subprocess

SAFE_COMMANDS = {
    "dir", "ipconfig", "echo", "ping", "netstat", "tasklist", "powershell",
    "shutdown", "start", "taskkill", "explorer"
}

def parse_command(text):
    """
    Procura por padrões 'run: <comando>'
    Ex.: 'run: ipconfig /all' -> 'ipconfig /all'
    """
    if "run:" in text.lower():
        cmd = text.split("run:")[1].strip()
        # Divida por espaços mas mantenha quotes
        return cmd
    return None

def is_safe(cmd):
    """Verifica se a primeira palavra do comando está na whitelist."""
    first_word = cmd.split()[0].lower()
    return first_word in SAFE_COMMANDS

def execute(cmd):
    if not is_safe(cmd):
        return f"⚠️ O comando '{cmd}' não está na lista de comandos permitidos."
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        output = result.stdout or result.stderr
        return output.strip() or "(sem saída)"
    except Exception as e:
        return f"⚠️ Erro ao executar: {e}"
