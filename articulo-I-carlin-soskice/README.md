# Artículo I — Código y reproducibilidad

## El modelo de tres ecuaciones de Carlin–Soskice: dinámica, estabilidad y adaptación de la política monetaria

Este directorio contiene los códigos, resultados numéricos y figuras utilizados para reproducir los ejercicios computacionales del Artículo I.

El análisis se centra en las propiedades de estabilidad, la naturaleza de los valores propios y los efectos de distintos grados de adaptación de la política monetaria.

## Estructura del repositorio

    articulo-I-carlin-soskice/
    ├── README.md
    ├── requirements.txt
    ├── python/
    │   ├── modelo_cs.py
    │   ├── figura_1_estabilidad.py
    │   ├── figura_2_radio_espectral.py
    │   ├── figuras_3_4_irf.py
    │   ├── figura_5_caso_D_inestabilidad.py
    │   └── generar_figuras.py
    ├── figuras/
    │   ├── figura_1_estabilidad.pdf/.svg
    │   ├── figura_2_radio_espectral.pdf/.svg
    │   ├── figura_3_irf_producto.pdf/.svg
    │   ├── figura_4_irf_inflacion.pdf/.svg
    │   └── figura_5_caso_D_inestabilidad.pdf/.svg
    └── resultados/
        ├── regimenes_dinamicos.csv
        └── irf_demanda_tres_regimenes.csv

Las figuras se distribuyen en formatos vectoriales PDF y SVG. El PDF es el formato utilizado por el manuscrito LaTeX; el SVG facilita la visualización y reutilización de las figuras fuera de LaTeX.

## Ejecución

Desde la carpeta del proyecto:

    cd articulo-I-carlin-soskice/python
    python generar_figuras.py

El script maestro genera las Figuras 1–5 y los resultados numéricos. Las figuras se guardan en figuras/ y los resultados en resultados/.

## Parámetros principales

La parametrización base utiliza alpha = 0.8, gamma = 0.8 y kappa = 0.5. Las Figuras 3 y 4 utilizan los tres regímenes A, B y C definidos en el artículo. La Figura 5 corresponde al caso D, con eta = 0.50 y s = 3.00.

## Shock

Las IRF utilizan un shock unitario de demanda d_0 = 1, representado mediante la condición inicial z_1=(1,kappa). A partir de ese momento, el sistema evoluciona como z_{t+1}=A z_t.

## Nota sobre las fronteras

Si se define a = alpha(1-eta), las principales fronteras analíticas son:

- discriminante nulo: s = (1 ± sqrt(a))^2;
- traza nula: s = 1 + a;
- frontera de estabilidad: s = 2(1+a).

La Figura 1 distingue la zona estable con valores propios reales, la zona estable con valores propios complejos y la zona inestable. La Figura 2 muestra directamente el radio espectral rho(A).

El repositorio complementa la versión LaTeX del artículo y permite reproducir las figuras y resultados numéricos reportados.
