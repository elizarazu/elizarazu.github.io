"""Genera la Figura 2: mapa del radio espectral."""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from modelo_cs import matriz_transicion

ALPHA, GAMMA, KAPPA = 0.8, 0.8, 0.5
eta = np.linspace(0.0, 1.0, 301)
s = np.linspace(0.0, 4.0, 301)
E, S = np.meshgrid(eta, s)
rho = np.empty_like(E)

for i in range(E.shape[0]):
    for j in range(E.shape[1]):
        A = matriz_transicion(ALPHA, GAMMA, KAPPA, E[i,j], S[i,j])
        rho[i,j] = np.max(np.abs(np.linalg.eigvals(A)))

a = ALPHA * (1.0 - eta)
s_minus = (1.0 - np.sqrt(a))**2
s_plus = (1.0 + np.sqrt(a))**2
s_stab = 2.0 * (1.0 + a)
s_T0 = 1.0 + a

fig, ax = plt.subplots(figsize=(8.6, 6.6))
cf = ax.contourf(E, S, rho, levels=np.linspace(0,1.6,17))
ax.plot(eta, s_minus, linewidth=2, label=r"$\Delta=0:\ s=(1-\sqrt{a})^2$")
ax.plot(eta, s_plus, linewidth=2, label=r"$\Delta=0:\ s=(1+\sqrt{a})^2$")
ax.plot(eta, s_stab, linewidth=2, label=r"Frontera de estabilidad")
ax.plot(eta, s_T0, "--", linewidth=1.5, label=r"$T=0:\ s=1+a$")
cbar = fig.colorbar(cf, ax=ax)
cbar.set_label(r"Radio espectral $\rho(A)$")
ax.set_xlabel(r"Adaptación monetaria, $\eta$")
ax.set_ylabel(r"Intensidad monetaria, $s=\kappa\gamma\phi_\pi$")
ax.set_title(r"Radio espectral del sistema dinámico ($\alpha=0.8$)")
ax.set_xlim(0,1); ax.set_ylim(0,4); ax.grid(True, alpha=0.2)
ax.legend(loc="upper right", frameon=True)
fig.tight_layout()
fig.savefig(ROOT / "figuras" / "figura_2_radio_espectral.pdf", bbox_inches="tight")
fig.savefig(ROOT / "figuras" / "figura_2_radio_espectral.png", dpi=300, bbox_inches="tight")
plt.close(fig)
