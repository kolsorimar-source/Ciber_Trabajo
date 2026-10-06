from datetime import datetime
import subprocess

usuario = subprocess.check_output(
    ["git", "config", "user.name"],
    text=True
).strip()

fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"Usuario: {usuario}")
print(f"Fecha: {fecha}")
