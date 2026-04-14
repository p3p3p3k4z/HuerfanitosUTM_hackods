# 📑 Reporte de Procesamiento y Validación de Datos (ODS 15)

Este reporte documenta el procedimiento técnico seguido para la generación de la base de datos del proyecto **HackODS UNAM 2026**. Se estructura siguiendo el plan modular aprobado para garantizar la trazabilidad y veracidad de la información.

---

## 1. Metodología de Procesamiento (ETL Modular)

Se implementó una arquitectura de **cinco componentes independientes** para evitar la contaminación de datos y facilitar la auditoría por tema:

### A. Módulo Maestro (Michoacán Local)
- **Script**: `etl_maestro_ods15.py`
- **Procedimiento**: 
    - Escaneo profundo de `data/crudos/` buscando archivos del Censo Agropecuario 2022.
    - Fusión de datos de producción (aguacate) con bases territoriales (superficies agrícolas y forestales).
    - **Cálculo de Alerta**: Generación del `impact_ratio` para detectar municipios con siembra excedente (posibles zonas de deforestación).

### B. Módulo de Contexto Nacional (La Exposición)
- **Script**: `etl_nacional_ods15.py`
- **Procedimiento**: 
    - Extracción de datos de las 32 entidades federativas.
    - Comparativa de la cuota de mercado de Michoacán frente al total nacional.
    - **Resultado**: Identificación de Michoacán como el líder con el 75% de la producción nacional.

### C. Módulo de Biodiversidad (Especies en Riesgo)
- **Script**: `etl_biodiversidad_ods15.py`
- **Procedimiento**: 
    - Procesamiento de `especies_arboles.xlsx`.
    - Agregación por volumen de madera de **Pino** y **Encino**.
    - **Relación Narrativa**: Estos ecosistemas templados son el hábitat principal de la mariposa monarca y las zonas más presionadas por el aguacate.

### D. Módulo de Gestión Ambiental (El Conflicto)
- **Script**: `etl_gestion_ambiental_ods15.py`
- **Procedimiento**: 
    - Cruce de unidades de producción forestal activas vs unidades con apoyo económico de CONAFOR.
    - **Hallazgo**: Solo un pequeño porcentaje de las unidades que realizan protección reciben financiamiento oficial.

### E. Módulo de Transparencia
- **Script**: `generate_metadata_transparencia.py`
- **Procedimiento**: Generación automática de un índice JSON que vincula cada variable con su archivo original fuente para auditoría de los jueces.

---

## 2. Validación de Veracidad

La información fue validada mediante un rigor de "tres pasos":

1.  **Integridad de Trazada**: Se seleccionó el dato de producción de aguacate de **Tancítaro** en el archivo crudo `ca2022_agr01.csv` (24,818.48 ha) y se comparó con el resultado del script. Coincidencia del 100%.
2.  **Lógica del Impact Ratio**: Se auditó el valor de **Ario de Rosales** (Ratio: 1.46). Se verificó que esta anomalía (más aguacate que tierra agrícola registrada) es un indicador verídico de cambio de uso de suelo en zonas boscosas.
3.  **Baselines ODS**: Las tasas de deforestación se cotejaron con los metadatos de la **Agenda 2030** para asegurar que el baseline nacional (-0.21%) sea el oficial vigente.

---

## 3. Inventario de Datos Generados

| Archivo | Nivel | Propósito |
| :--- | :--- | :--- |
| `dataset_maestro_ods15.csv` | Municipal | Análisis profundo de Michoacán. |
| `contexto_nacional_ods15.csv` | Estatal | Comparativa regional y dominancia. |
| `biodiversidad_especies_ods15.csv`| Biológico | Costo ecosistémico (Pino/Encino). |
| `gestion_ambiental_ods15.csv` | Político | Brecha de financiamiento y protección. |
| `impact_coefficients.json` | Técnico | Constantes para la calculadora de impacto. |
| `fuentes_metadata_ods15.json` | Auditoría | Transparencia y orígenes de datos. |

---

## 4. Estándares de Calidad
- **Gestión**: Todas las dependencias se manejan vía `uv` para reproducibilidad total.
- **Documentación**: Código con Type Hinting y Google-style docstrings.
- **Normalización**: Codificación UTF-8 y nombres de columnas autodescriptivos en español.

---
> [!IMPORTANT]
> **Nota para fases posteriores**: Estos datos están listos para ser consumidos por el dashboard en Quarto. La relación entre ellos permite construir la narrativa de la pirámide de Freytag de forma fluida y respaldada por evidencia estadística oficial.
