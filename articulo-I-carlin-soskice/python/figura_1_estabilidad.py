"""Genera la Figura 1: estabilidad y naturaleza de los valores propios."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
ALPHA = 0.8

eta = np.linspace(0.0, 1.0, 501)
s = np.linspace(0.0, 4.0, 501)
E, S = np.meshgrid(eta, s)

a = ALPHA * (1.0 - eta)
s_minus = (1.0 - np.sqrt(a)) ** 2
s_plus = (1.0 + np.sqrt(a)) ** 2
s_stab = 2.0 * (1.0 + a)
s_T0 = 1.0 + a

# 0: estable-real inferior; 1: estable-complejo;
# 2: estable-real superior; 3: inestable.
region = np.full(E.shape, 3, dtype=int)
region[(S > 0) & (S < s_stab[None, :])] = 2
region[(S > s_minus[None, :]) & (S < s_plus[None, :])] = 1
region[(S > 0) & (S <= s_minus[None, :])] = 0

fig, ax = plt.subplots(figsize=(8.6, 6.6))
ax.contourf(
    E, S, region,
    levels=[-0.5, 0.5, 1.5, 2.5, 3.5],
    alpha=0.16,
)

ax.plot(eta, s_minus, linewidth=2, label=r"$Delta=0: s=(1-sqrt{a})^2$")
ax.plot(eta, s_plus, linewidth=2, label=r"$Delta=0: s=(1+sqrt{a})^2$")
ax.plot(eta, s_stab, linewidth=2, label=r"Frontera de estabilidad")
ax.plot(eta, s_T0, "--", linewidth=1.5, label=r"$T=0: s=1+a$")

ax.set_xlabel(r"Adaptación monetaria, $eta$")
ax.set_ylabel(r"Intensidad monetaria, $s=kappagammaphi_pi$")
ax.set_title(r"Estabilidad y naturaleza de la dinámica ($alpha=0.8$)")
ax.set_xlim(0, 1)
ax.set_ylim(0, 4)
ax.grid(True, alpha=0.25)
ax.legend(loc="upper right", frameon=True)
fig.tight_layout()

output = ROOT / "figuras"
output.mkdir(parents=True, exist_ok=True)
fig.savefig(output / "figura_1_estabilidad.pdf", bbox_inches="tight")
fig.savefig(output / "figura_1_estabilidad.svg", bbox_inches="tight")
plt.close(fig)
