# Memoria de Trabajo: Trabajo Práctico N° 3 - Medidas Electrónicas I

Esta memoria documenta las actividades, cálculos, mediciones y modificaciones de formato realizadas sobre el informe del Trabajo Práctico N° 3: *"Medición de parámetros de amplificadores. Uso de escala en dB. Efecto de la realimentación negativa"* de la materia **Medidas Electrónicas I (UTN-FRC)**.

---

## 1. Sesión Anterior: Caracterización y Respuestas Espectrales

Durante la primera fase del desarrollo del informe, se completaron los Experimentos 4, 5, 6 y 7, y se resolvieron errores estructurales de LaTeX:

### Experimento 4: Medición de Ganancia y Potencia
* **Cálculos**: Se determinaron las potencias reales en $\dBm$ a partir de niveles medidos en $\dBu$ (referenciados a $600\ohm$):
  $$P_{\text{ent}} [\dBm] = -1\dBu + 10\log_{10}\left(\frac{600\ohm}{1096\ohm}\right) = -3.62\dBm$$
  $$P_{\text{sal}} [\dBm] = 7.2\dBu + 10\log_{10}\left(\frac{600\ohm}{42\ohm}\right) = 18.75\dBm$$
* **Resultados**: Ganancia de tensión $A_v = 8.2\dB$ ($2.57$ veces); Ganancia de potencia $A_p = 22.37\dB$ ($172.4$ veces).
* Se completó la tabla `tab:exp4` ajustando su ancho y agregando el desarrollo de los cálculos paso a paso.

### Experimento 5: Resistencia de Salida
* **Lazo Abierto**: Con $V_i = 42\mV_{pp}$, $V_{o,\text{vacío}} = 7.2\V_{pp}$ y $V_s = 4.64\V_{pp}$ sobre $R_L = 1\k\ohm$:
  $$A = 171.43, \quad R_o = \left(\frac{V_{o,\text{vacío}}}{V_s} - 1\right)R_L = 551.7\ohm$$
* **Lazo Cerrado**: Con $V_i = 40.8\mV_{pp}$ y $V_o' = 440\mV_{pp}$ en vacío:
  $$G = 10.78, \quad R_{o,\text{calc}}' = \frac{R_o}{1 + A \beta} = 34.7\ohm$$
  Para el cálculo experimental con $V_s' = 190\mV_{pp}$ y $R_L = 33\ohm$:
  $$R_{o,\text{exp}}' = \left(\frac{V_o'}{V_s'} - 1\right)R_L = 43.4\ohm$$
* **Imágenes**: Se convirtieron los oscilogramas a PNG e incluyeron:
  * `osc_exp5_vo_vacio.png`
  * `osc_exp5_vrl_1k.png`
  * `osc_exp5_vof_vacio.png`
  * `osc_exp5_vrl_realim_33ohm.png`

### Experimento 6: Máxima Excursión Simétrica
* **Cálculos de Potencia Máxima**:
  * **Lazo Abierto**: $P_{\text{máx,LA}} = \frac{V_{o,\text{max}}^2}{8 R_L} = 2.83\mW$ (con $V_{o,\text{max}} = 3.56\V_{pp}$ sobre $R_L = 560\ohm$).
  * **Lazo Cerrado**: $P_{\text{máx,LC}} = \frac{(V_{o,\text{max}}')^2}{8 R_L} = 0.82\mW$ (con $V_{o,\text{max}}' = 464\mV_{pp}$ sobre $R_L = 33\ohm$).
* Se actualizó la tabla `tab:exp6` (removiendo la columna redundante de $V_{rms}$) e incluyeron las capturas correspondientes.

### Experimento 7: Respuesta en Frecuencia (Barrido Senoidal)
* Se calcularon los niveles de atenuación de $-2\dB$ y $-3\dB$ respecto de las tensiones de referencia de $1\kHz$:
  * **Lazo Abierto** ($V_o(1\kHz) = 7.2\V_{pp}$): $V_o(-2\dB) = 5.72\V_{pp}$, $V_o(-3\dB) = 5.10\V_{pp}$.
  * **Lazo Cerrado** ($V_o'(1\kHz) = 8.16\V_{pp}$): $V_o'(-2\dB) = 6.48\V_{pp}$, $V_o'(-3\dB) = 5.78\V_{pp}$.
* Se completaron las tablas `tab:exp7_abierto` y `tab:exp7_cerrado` agregando puntos intermedios y aplicando `\resizebox{\textwidth}{!}{...}`.
* Se graficaron ambas respuestas en frecuencia superpuestas usando el paquete **PGFPlots/TikZ** (`fig:respuesta_frecuencia_comparativa`), estableciendo escalas logarítmicas idénticas en el eje horizontal.

---

## 2. Sesión Actual: Respuesta Temporal, Incertidumbres e Instrumentación

En la sesión de hoy, se completaron los aspectos de respuesta al escalón, estimación de incertidumbres del Experimento 2 y la sección de equipamiento del laboratorio:

### Experimento 8: Respuesta al Escalón (Onda Cuadrada)
* **Parámetros de Entrada**:
  * Ancho de banda del osciloscopio: $AB_{\text{osc}} = 50\MHz \implies t_{c,\text{osc}} = 7\ns$.
  * Tiempo de crecimiento medido a lazo abierto: $t_{c,\text{medido, LA}} = 4.4\us$.
  * Tiempo de crecimiento medido a lazo cerrado: $t_{c,\text{medido, LC}} = 190\ns$.
* **Cálculos de Tiempo Propio y Ancho de Banda**:
  * **Lazo Abierto**: $t_{c,\text{amplif, LA}} \approx 4.4\us \implies AB_{\text{cuadrada, LA}} \approx 79.55\kHz$.
  * **Lazo Cerrado**: $t_{c,\text{amplif, LC}} = \sqrt{(190\ns)^2 - (7\ns)^2} \approx 189.87\ns \implies AB_{\text{cuadrada, LC}} \approx 1.84\MHz$.
* **Inclusión de Imágenes**: Se agregaron las capturas `osc_exp8_tr_la.png` y `osc_exp8_tr_lc.png`.
* **Justificación del factor $k=0.35$**: Se redactó la explicación física del factor de proporcionalidad y se diseñó una comparación gráfica en **TikZ** (Figura~\ref{fig:comparacion_k_sobreimpulso}) mostrando en tiempo y frecuencia la caída suave (exponencial, $k=0.35$) frente al comportamiento subamortiguado con sobreimpulso (*peaking/ringing*, $k=0.40$).
* Se actualizó la tabla `tab:exp8` con unidades duales y corrección de desborde de márgenes.

### Experimento 2: Incertidumbre de $R_{e1} = R_i$
* **Parámetros**: Multímetro en rango de $2000\ohm$, precisión $\pm(0.7\% + 2)$ y resolución $1\ohm$.
* **Cálculo de Incertidumbre Absoluta**:
  $$\Delta R_{e1} = \pm (0.007 \cdot 1096\ohm + 2 \cdot 1\ohm) = \pm (7.672\ohm + 2\ohm) = \pm 9.672\ohm$$
* **Ajuste y Tabla**: Expresado según la resolución del equipo, se determinó $\Delta R_{e1} = \pm 10\ohm$. Se redactó la justificación matemática y se completó la Tabla~\ref{tab:exp2} con el valor final.

### Creación del Capítulo de Instrumentación Utilizada
* Se creó el archivo `chapters/3-instrumentacion.tex` que actúa como el **Capítulo 3** del informe.
* Este capítulo describe brevemente los equipos utilizados:
  1. Osciloscopio digital **Rigol DS1052E**.
  2. Generador de funciones **GW Instek SFG-2120**.
  3. Multímetro analógico **UNIVO**.
  4. Multímetro digital **UNI-T UT33A+**.
  5. Fuente de alimentación regulada continua del laboratorio central.
* Se agregó la línea `\input{chapters/3-instrumentacion.tex}` en `main.tex`.

---

## 3. Estado del Proyecto y Verificación de Compilación

* **Compilación**: Limpia y exitosa tras ejecutar `make clean && make`. El documento [MedidasElectronicas1_tp3.pdf](file:///home/angeloprieto/Desktop/Facu/4to/MedElec/MedidasElectronicas1/tp3/MedidasElectronicas1_tp3.pdf) se genera con un total de 30 páginas.
* **Advertencias**: Se resolvieron todas las advertencias críticas de márgenes (`Overfull \hbox`) de tablas re-estructurando sus celdas y envolviéndolas en entornos `\resizebox`.
* **Imágenes**: Todas las capturas del osciloscopio se encuentran vinculadas en formato PNG para evitar errores de compilación con `pdflatex`.
