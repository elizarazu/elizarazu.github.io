# Artículo I — Código y reproducibilidad

## El modelo de tres ecuaciones de Carlin–Soskice: dinámica, estabilidad y adaptación de la política monetaria

Este directorio contiene los códigos, resultados numéricos y figuras utilizados para reproducir los ejercicios computacionales del Artículo I.

El artículo estudia una extensión dinámica del modelo de tres ecuaciones de Carlin–Soskice mediante la introducción de persistencia autorregresiva en la brecha del producto. El análisis se centra en las propiedades de estabilidad, la naturaleza de los valores propios y los efectos de distintos grados de adaptación de la política monetaria.

---

## Estructura del repositorio

```text
articulo-I-carlin-soskice/
│
├── README.md
├── requirements.txt
│
├── python/
│   ├── modelo_cs.py
│   ├── figura_1_estabilidad.py
│   ├── figura_2_radio_espectral.py
│   ├── figuras_3_4_irf.py
│   ├── figura_5_caso_D_inestabilidad.py
│   └── generar_figuras.py
│
├── figuras/
│   ├── figura_1_estabilidad.pdf/.png
│   ├── figura_2_radio_espectral.pdf/.png
│   ├── figura_3_irf_producto.pdf/.png
│   ├── figura_4_irf_inflacion.pdf/.png
│   └── figura_5_caso_D_inestabilidad.pdf/.png
│
└── resultados/
    ├── regimenes_dinamicos.csv
    └── irf_demanda_tres_regimenes.csv
```

## Ejecución

Desde la carpeta `python/`:

```bash
python generar_figuras.py
```

El script maestro genera las Figuras 1–5 y los resultados numéricos. Las figuras se guardan en `figuras/` y los resultados en `resultados/`.

## Parámetros principales

La parametrización base utiliza `alpha = 0.8`, `gamma = 0.8` y `kappa = 0.5`. Las Figuras 3 y 4 utilizan los tres regímenes A, B y C definidos en el artículo. La Figura 5 corresponde al caso D, una configuración inestable con `eta = 0.50` y `s = 3.00`.

## Shock

Las IRF utilizan un shock unitario de demanda `d_0 = 1`, con `d_t = 0` para `t >= 1`, partiendo del equilibrio.

La Figura 5 utiliza la misma condición inicial y muestra la trayectoria del sistema cuando el radio espectral es `rho(A) = 1.2899 > 1`.

El repositorio complementa la versión LaTeX del artículo y permite reproducir las figuras y resultados numéricos reportados.
