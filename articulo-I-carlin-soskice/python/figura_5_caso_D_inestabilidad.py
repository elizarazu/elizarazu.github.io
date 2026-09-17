"""Genera la Figura 5: respuesta del sistema en el caso D (inestable)."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]


def matriz_transicion(alpha, gamma, kappa, eta, s):
    phi_x = eta * alpha / gamma
    phi_pi = s / (kappa * gamma)
    a = alpha - gamma * phi_x
    return np.array([[a, -gamma * phi_pi], [kappa * a, 1.0 - kappa * gamma * phi_pi]])


ALPHA, GAMMA, KAPPA = 0.8, 0.8, 0.5
ETA, S = 0.50, 3.00
PERIODS = 30

A = matriz_transicion(ALPHA, GAMMA, KAPPA, ETA, S)
eig = np.linalg.eigvals(A)
rho = np.max(np.abs(eig))

t = np.arange(PERIODS + 1)
z = np.zeros((PERIODS + 1, 2))
z[1, :] = np.array([1.0, KAPPA])
for i in range(1, PERIODS):
    z[i + 1, :] = A @ z[i, :]

fig, axes = plt.subplots(2, 1, figsize=(8.6, 7.0), sharex=True)
axes[0].plot(t, z[:, 0], linewidth=1.8)
axes[0].axhline(0, linewidth=0.8)
axes[0].set_ylabel(r"Brecha del producto, $x_t$")
axes[0].set_title(r"Caso D: dinámica inestable ($\eta=0.50$, $s=3.00$, $\rho(A)=%.4f$)" % rho)
axes[0].grid(True, alpha=0.25)

axes[1].plot(t, z[:, 1], linewidth=1.8)
axes[1].axhline(0, linewidth=0.8)
axes[1].set_xlabel(r"Período, $t$")
axes[1].set_ylabel(r"Desviación de inflación, $\widetilde{\pi}_t$")
axes[1].grid(True, alpha=0.25)
axes[1].set_xlim(0, PERIODS)

fig.tight_layout()
fig.savefig(ROOT / "figuras" / "figura_5_caso_D_inestabilidad.pdf", bbox_inches="tight")
fig.savefig(ROOT / "figuras" / "figura_5_caso_D_inestabilidad.png", dpi=300, bbox_inches="tight")
plt.close(fig)
print(f"Figura 5 generada. rho(A)={rho:.4f}")
