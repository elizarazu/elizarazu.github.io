"""Script maestro: genera las Figuras 1--4 y los resultados numéricos."""

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
scripts = [
    "figura_1_estabilidad.py",
    "figura_2_radio_espectral.py",
    "figuras_3_4_irf.py",
]

for script in scripts:
    subprocess.run([sys.executable, str(HERE / script)], check=True)

print("Figuras 1--4 y resultados numéricos generados correctamente.")
