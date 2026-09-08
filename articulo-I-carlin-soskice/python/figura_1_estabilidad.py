"""Genera la Figura 1: mapa de estabilidad y naturaleza de los valores propios."""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from modelo_cs import matriz_transicion

ALPHA, GAMMA, KAPPA = 0.8, 0.8, 0.5
eta = np.linspace(0.0, 1.0, 501)
s = np.linspace(0.0, 4.0, 501)
E, S = np.meshgrid(eta, s)
a = ALPHA * (1.0 - E)
s_minus = (1.0 - np.sqrt(a))**2
s_plus = (1.0 + np.sqrt(a))**2
s_stab = 2.0 * (1.0 + a)
s_T0 = 1.0 + a

region = np.full(E.shape, 3)
region[(S < s_stab) & (S >= s_plus)] = 2
region[(S < s_plus) & (S > s_minus)] = 1
region[(S <= s_minus) & (S >= 0)] = 0

fig, ax = plt.subplots(figsize=(8.6, 6.6))
ax.contourf(E, S, region, levels=[-0.5,0.5,1.5,2.5,3.5], alpha=0.16)
ax.plot(eta, s_minus[0], linewidth=2, label=r"$s=(1-\sqrt{a})^2$")
ax.plot(eta, s_plus[0], linewidth=2, label=r"$s=(1+\sqrt{a})^2$")
ax.plot(eta, s_stab[0], linewidth=2, label=r"$s=2(1+a)$")
ax.plot(eta, s_T0[0], "--", linewidth=1.5, label=r"$T=0:\ s=1+a$")
ax.set_xlabel(r"Adaptación monetaria, $\eta$")
ax.set_ylabel(r"Intensidad monetaria, $s=\kappa\gamma\phi_\pi$")
ax.set_title(r"Mapa de estabilidad y dinámica ($\alpha=0.8$)")
ax.set_xlim(0,1); ax.set_ylim(0,4); ax.grid(True, alpha=0.25)
ax.legend(loc="upper right", frameon=True)
fig.tight_layout()
fig.savefig(ROOT / "figuras" / "figura_1_estabilidad.pdf", bbox_inches="tight")
fig.savefig(ROOT / "figuras" / "figura_1_estabilidad.png", dpi=300, bbox_inches="tight")
plt.close(fig)
