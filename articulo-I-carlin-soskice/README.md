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
│   └── generar_figuras.py
│
├── figuras/
│   ├── figura_1_estabilidad.pdf
│   ├── figura_1_estabilidad.png
│   ├── figura_2_radio_espectral.pdf
│   ├── figura_2_radio_espectral.png
│   ├── figura_3_irf_producto.pdf
│   ├── figura_3_irf_producto.png
│   ├── figura_4_irf_inflacion.pdf
│   └── figura_4_irf_inflacion.png
│
└── resultados/
    ├── regimenes_dinamicos.csv
    └── irf_demanda_tres_regimenes.csv
