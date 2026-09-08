"""Genera las Figuras 3 y 4: IRF de producto e inflación."""
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from modelo_cs import indicadores_dinamicos, respuesta_demanda

ALPHA, GAMMA, KAPPA = 0.8, 0.8, 0.5
PERIODS = 40
CASES = {
    "A": {"eta": 0.10, "s": 0.005},
    "B": {"eta": 0.50, "s": 1.500},
    "C": {"eta": 0.90, "s": 0.450},
}

rows = []
trajectories = {}
for case, pars in CASES.items():
    t, z = respuesta_demanda(ALPHA, GAMMA, KAPPA, pars["eta"], pars["s"], periods=PERIODS)
    ind = indicadores_dinamicos(ALPHA, GAMMA, KAPPA, pars["eta"], pars["s"])
    trajectories[case] = (t, z)
    rows.append({
        "Caso": case, "eta": pars["eta"], "s": pars["s"],
        "phi_x": pars["eta"]*ALPHA/GAMMA,
        "phi_pi": pars["s"]/(KAPPA*GAMMA),
        "a": ALPHA*(1-pars["eta"]), "T": ind["T"], "D": ind["D"],
        "Delta": ind["Delta"], "lambda_1": ind["lambda_1"],
        "lambda_2": ind["lambda_2"], "rho_A": ind["rho"]
    })

pd.DataFrame(rows).to_csv(ROOT / "resultados" / "regimenes_dinamicos.csv", index=False)
irf = pd.DataFrame({"t": trajectories["A"][0]})
for case, (t, z) in trajectories.items():
    irf[f"x_{case}"] = z[:,0]
    irf[f"pi_{case}"] = z[:,1]
irf.to_csv(ROOT / "resultados" / "irf_demanda_tres_regimenes.csv", index=False)

for variable, ylabel, title, filename in [
    ("x", r"Brecha del producto, $x_t$", r"IRF ante un shock de demanda $d_0=1$", "figura_3_irf_producto"),
    ("pi", r"Desviación de inflación, $\widetilde{\pi}_t$", r"IRF de la inflación ante un shock de demanda $d_0=1$", "figura_4_irf_inflacion")]:
    fig, ax = plt.subplots(figsize=(8.6,5.0))
    for case, (t,z) in trajectories.items():
        pars = CASES[case]
        ax.plot(t, z[:,0] if variable == "x" else z[:,1], linewidth=1.8,
                label=fr"Caso {case}: $\eta={pars['eta']:.1f}$, $s={pars['s']:g}$")
    ax.axhline(0, linewidth=0.8)
    ax.set_xlabel(r"Período, $t$"); ax.set_ylabel(ylabel); ax.set_title(title)
    ax.set_xlim(0, PERIODS); ax.grid(True, alpha=0.25); ax.legend(loc="upper right")
    fig.tight_layout()
    fig.savefig(ROOT / "figuras" / f"{filename}.pdf", bbox_inches="tight")
    fig.savefig(ROOT / "figuras" / f"{filename}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)
