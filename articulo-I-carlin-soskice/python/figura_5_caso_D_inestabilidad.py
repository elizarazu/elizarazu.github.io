"""Genera la Figura 5: respuesta del sistema en el caso D (inestable)."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from modelo_cs import indicadores_dinamicos, respuesta_demanda

ALPHA, GAMMA, KAPPA = 0.8, 0.8, 0.5
ETA, S = 0.50, 3.00
PERIODS = 30
ZOOM_PERIODS = 15

ind = indicadores_dinamicos(ALPHA, GAMMA, KAPPA, ETA, S)
t, z = respuesta_demanda(ALPHA, GAMMA, KAPPA, ETA, S, periods=PERIODS)

fig, axes = plt.subplots(2, 1, figsize=(8.6, 7.0), sharex=True)

axes[0].plot(t, z[:, 0], color="black", linewidth=1.8)
axes[0].axhline(0, color="black", linewidth=0.8)
axes[0].set_ylabel(r"Brecha del producto, $x_t$")
axes[0].set_title(
    r"Caso D: dinámica inestable "
    r"($\eta=0.50$, $s=3.00$, $\rho(A)=%.4f$)" % ind["rho"]
)
axes[0].grid(True, color="0.80", linewidth=0.6, alpha=0.8)
axes[0].set_xlim(0, PERIODS)

# Inserto compacto, ligeramente desplazado para no interferir con el eje principal.
axins1 = inset_axes(
    axes[0], width="29%", height="38%", loc="upper left",
    bbox_to_anchor=(0.045, -0.015, 1, 1),
    bbox_transform=axes[0].transAxes, borderpad=0.8,
)
axins1.plot(t[:ZOOM_PERIODS + 1], z[:ZOOM_PERIODS + 1, 0],
            color="black", linewidth=1.1)
axins1.axhline(0, color="black", linewidth=0.5)
axins1.grid(True, color="0.85", linewidth=0.45, alpha=0.8)
axins1.set_xlim(0, ZOOM_PERIODS)
axins1.set_title("Primeros 15 períodos", fontsize=7.5, pad=2)
axins1.tick_params(labelsize=6.5, pad=1)

axes[1].plot(t, z[:, 1], color="black", linewidth=1.8)
axes[1].axhline(0, color="black", linewidth=0.8)
axes[1].set_xlabel(r"Período, $t$")
axes[1].set_ylabel(r"Desviación de inflación, $\widetilde{\pi}_t$")
axes[1].grid(True, color="0.80", linewidth=0.6, alpha=0.8)
axes[1].set_xlim(0, PERIODS)

axins2 = inset_axes(
    axes[1], width="29%", height="38%", loc="upper left",
    bbox_to_anchor=(0.045, -0.015, 1, 1),
    bbox_transform=axes[1].transAxes, borderpad=0.8,
)
axins2.plot(t[:ZOOM_PERIODS + 1], z[:ZOOM_PERIODS + 1, 1],
            color="black", linewidth=1.1)
axins2.axhline(0, color="black", linewidth=0.5)
axins2.grid(True, color="0.85", linewidth=0.45, alpha=0.8)
axins2.set_xlim(0, ZOOM_PERIODS)
axins2.set_title("Primeros 15 períodos", fontsize=7.5, pad=2)
axins2.tick_params(labelsize=6.5, pad=1)

fig.tight_layout()

output = ROOT / "figuras"
output.mkdir(parents=True, exist_ok=True)
fig.savefig(output / "figura_5_caso_D_inestabilidad.pdf", bbox_inches="tight")
fig.savefig(output / "figura_5_caso_D_inestabilidad.svg", bbox_inches="tight")
plt.close(fig)

print(f"Figura 5 generada. rho(A)={ind['rho']:.4f}")
