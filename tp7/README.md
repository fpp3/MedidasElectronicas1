# Trabajo Práctico de Laboratorio N° 7: Medición y Análisis de Señales con Osciloscopio de Almacenamiento Digital (DSO)

**Cátedra:** Medidas Electrónicas I  
**Institución:** Universidad Tecnológica Nacional - Facultad Regional Córdoba (UTN-FRC)  
**Comisión:** 4R2  
**Año:** 2026  

---

## Integrantes y Asignación de Roles
* **Encargado de Calidad y Gestión (ECG):** Angelo Prieto (Legajo: 401012)
* **Encargado de Operaciones y Mediciones (EO):** Franco Palombo (Legajo: 401910)
* **Encargado de Documentación y Cálculos (ED):** Gaston Grasso (Legajo: 401892)

---

## Estructura del Directorio
* `main.tex`: Archivo maestro del documento LaTeX basado en `informeutn.cls`.
* `Makefile`: Automatización de compilación con `latexmk`.
* `fuentes.bib`: Bibliografía de referencia (hojas de datos, manuales de usuario y textos de DSP/medidas).
* `chapters/`:
  * `1-integrantes.tex`: Conformación del grupo de trabajo y matriz de responsabilidades.
  * `2-introduccion.tex`: Fundamentación teórica (DFT/FFT, aliasing, enventanado, AM, FM/Bessel, IMD3, THD).
  * `3-materiales.tex`: Instrumental de laboratorio (Tektronix TDS 1001, Rigol DS1052E, generadores Instek, UT89X) y circuitos bajo prueba.
  * `4-desarrollo.tex`: Procedimiento experimental detallado de las 7 experiencias de laboratorio.
  * `5-conclusiones.tex`: Análisis crítico de resultados, tabla comparativa de ventanas y respuestas a la consigna.
  * `6-anexos.tex`: Especificaciones de instrumentos, formulario de conversión de dBV/dBm y tabla de coeficientes de Bessel.
* `figures/`: Diagramas esquemáticos en CircuiTikZ y diagramas de bloques en TikZ.
* `pictures/`: Fotografías del instrumental y capturas oscilográficas del laboratorio.
* `sources/`: Documentación base provista por la cátedra y fotos originales de relevamiento.

---

## Compilación
Para compilar el informe y generar `MedidasElectronicas1_tp7.pdf`:
```bash
make
```
Para limpiar archivos auxiliares de compilación manteniendo el PDF final:
```bash
latexmk -c -jobname=MedidasElectronicas1_tp7 main.tex
```
