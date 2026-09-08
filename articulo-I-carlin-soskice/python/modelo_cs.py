"""Funciones centrales del sistema dinámico del Artículo I."""
import numpy as np

def matriz_transicion(alpha, gamma, kappa, eta, s):
    phi_x = eta * alpha / gamma
    phi_pi = s / (kappa * gamma)
    a = alpha - gamma * phi_x
    return np.array([[a, -gamma * phi_pi], [kappa * a, 1.0 - kappa * gamma * phi_pi]])

def indicadores_dinamicos(alpha, gamma, kappa, eta, s):
    A = matriz_transicion(alpha, gamma, kappa, eta, s)
    eig = np.linalg.eigvals(A)
    T = np.trace(A); D = np.linalg.det(A); Delta = T**2 - 4*D
    return {"A": A, "T": T, "D": D, "Delta": Delta,
            "lambda_1": eig[0], "lambda_2": eig[1], "rho": np.max(np.abs(eig))}

def respuesta_demanda(alpha, gamma, kappa, eta, s, periods=40):
    A = matriz_transicion(alpha, gamma, kappa, eta, s)
    z = np.zeros((periods + 1, 2)); z[1, :] = np.array([1.0, kappa])
    for t in range(1, periods): z[t+1, :] = A @ z[t, :]
    return np.arange(periods + 1), z
