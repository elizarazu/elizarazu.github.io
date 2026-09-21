"""Genera la Figura 5: respuesta del sistema en el caso D (inestable)."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from modelo_cs import indicadores_dinamicos, respuesta_demanda

ALPHA, GAMMA, KAPPA = 0.8, 0.8, 0.5
ETA, S = 0.50, 3.00
PERIODS = 30

ind = indicadores_dinamicos(ALPHA, GAMMA, KAPPA, ETA, S)
t, z = respuesta_demanda(ALPHA, GAMMA, KAPPA, ETA, S, periods=PERIODS)

fig, axes = plt.subplots(2, 1, figsize=(8.6, 7.0), sharex=True)

axes[0].plot(t, z[:, 0], linewidth=1.8)
axes[0].axhline(0, linewidth=0.8)
axes[0].set_ylabel(r"Brecha del producto, $x_t$")
axes[0].set_title(
    r"Caso D: dinámica inestable "
    r"($eta=0.50$, $s=3.00$, $ho(A)=%.4f$)" % ind["rho"]
)
axes[0].grid(True, alpha=0.25)

axes[1].plot(t, z[:, 1], linewidth=1.8)
axes[1].axhline(0, linewidth=0.8)
axes[1].set_xlabel(r"Período, $t$")
axes[1].set_ylabel(r"Desviación de inflación, $widetilde{pi}_t$")
axes[1].grid(True, alpha=0.25)
axes[1].set_xlim(0, PERIODS)

fig.tight_layout()

output = ROOT / "figuras"
output.mkdir(parents=True, exist_ok=True)
fig.savefig(output / "figura_5_caso_D_inestabilidad.pdf", bbox_inches="tight")
fig.savefig(output / "figura_5_caso_D_inestabilidad.svg", bbox_inches="tight")
plt.close(fig)

print(f"Figura 5 generada. rho(A)={ind['rho']:.4f}")
