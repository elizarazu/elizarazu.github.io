# Artículo I — Código y reproducibilidad

**El modelo de tres ecuaciones de Carlin–Soskice: dinámica, estabilidad y adaptación de la política monetaria**

Este directorio contiene el código Python utilizado para reproducir las simulaciones, figuras y resultados numéricos del Artículo I.

## Estructura

- `python/`: código del modelo y scripts de las Figuras 1–4.
- `figuras/`: figuras generadas en PDF y PNG.
- `resultados/`: resultados numéricos y trayectorias de las IRF.
- `requirements.txt`: dependencias mínimas de Python.

## Ejecución

Desde la carpeta `python/`:

```bash
python generar_figuras.py
```

Las figuras se guardan en `figuras/` y los resultados numéricos en `resultados/`.

## Parámetros principales

La simulación usa `alpha = 0.8`, `gamma = 0.8` y `kappa = 0.5`, con la parametrización del artículo y los tres regímenes A, B y C.

## Shock

Las IRF utilizan un shock unitario de demanda `d_0 = 1`, con `d_t = 0` para `t >= 1`, partiendo del equilibrio.

El repositorio está preparado para complementar la versión LaTeX del artículo y facilitar la reproducibilidad de las figuras y resultados reportados.
