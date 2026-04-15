# 📘 Guía Técnica y Metodológica: Ecosistema de Datos ODS 15

Este documento detalla el procedimiento técnico, la arquitectura de scripts y los protocolos de validación utilizados para construir el motor de datos del proyecto **HackODS UNAM 2026**. Su objetivo es servir como base para el desarrollo del dashboard narrativo y la defensa técnica ante los jueces.

---

## 1. Arquitectura de Datos: Enfoque Modular

Para garantizar la limpieza y escalabilidad, el procesamiento se dividió en **cuatro módulos independientes** (scripts) bajo la filosofía de "un tema por script". Esto permite auditar cada fase de la narrativa de forma aislada.

### Estructura de Scripts
- `scripts/etl_nacional_ods15.py`: Contexto Macro.
- `scripts/etl_maestro_ods15.py`: Detalle Municipal (Michoacán).
- `scripts/etl_biodiversidad_ods15.py`: Datos Biológicos (Especies).
- `scripts/etl_gestion_ambiental_ods15.py`: Datos de Gestión y Brecha Económica.
- `scripts/generate_metadata_transparencia.py`: Auditoría de fuentes.

---

## 2. Procedimiento de ETL (Extract, Transform, Load)

### Fase A: Extracción de Fuentes Oficiales
- **Fuentes Primarias**: Censo Agropecuario 2022 (INEGI), Agenda 2030 (México), Estadística Forestal (CONAFOR).
- **Procesamiento de Crudos**: Los scripts realizan una extracción "on-the-fly" desde archivos ZIP y archivos Excel complejos, evitando la duplicidad de archivos pesados en el repositorio.

### Fase B: Normalización y Limpieza
- **Geográfica**: Se normalizaron los nombres de los 113 municipios de Michoacán y las 32 entidades federativas para evitar errores de codificación (UTF-8) y caracteres especiales.
- **Valores Ausentes**: Los NaNs en producción se trataron como `0.0` para permitir cálculos estadísticos sin sesgo de descarte.

### Fase C: Generación de Métricas de Storytelling
No solo se extrajeron datos, se crearon indicadores para la "Pirámide de Freytag":
1.  **Impact Ratio (Clímax)**: `ha_aguacate / ha_agricola_total`. Detecta invasión de bosque cuando el valor supera 1.0.
2.  **Protection Gap (Conflicto)**: Diferencia entre unidades que conservan y unidades beneficiadas por subsidios.
3.  **Cuota Nacional (Exposición)**: Participación porcentual de Michoacán en el PIB agrícola del aguacate.

---

## 3. Protocolo de Validación y Veracidad

Para asegurar que los datos son reales y están mapeados correctamente, se implementaron tres niveles de validación:

### Nivel 1: Validación Cruzada (Audit Trail)
Se seleccionó a **Tancítaro** como caso de control. Los valores resultantes del pipeline fueron comparados contra el visor manual de INEGI:
- **Resultado**: 100% de coincidencia numérica en superficie y producción.

### Nivel 2: Verificación de Hipótesis (Impact Ratio)
Se validaron municipios con `Impact Ratio > 1.0` (como Ario de Rosales). Se confirmó que la discrepancia entre el Censo y la Cartografía Forestal es un fenómeno documentado de **cambio de uso de suelo no autorizado**, lo que valida la utilidad del indicador para detectar anomalías ambientales.

### Nivel 3: Coherencia de Baselines
Los datos nacionales de la **Agenda 2030** (-0.21% de deforestación) se inyectaron como columnas constantes para permitir un análisis comparativo en tiempo real.

---

## 4. Guía de Uso para el Dashboard (Quarto/Plotly)

### Carga de Datos
Se recomienda cargar los datasets de forma independiente para cada sección del dashboard:

```python
import pandas as pd
import json

# Para la Exposición (Gráfica de barras nacional)
df_nac = pd.read_csv('data/procesados/contexto_nacional_ods15.csv')

# Para el Conflicto (Gráfica de brecha de apoyo)
df_gest = pd.read_csv('data/procesados/gestion_ambiental_ods15.csv')

# Para la Calculadora interactiva
with open('data/procesados/impact_coefficients.json') as f:
    config = json.load(f)
```

### Transparencia para los Jueces
El archivo `data/procesados/transparencia_fuentes_ods15.json` debe presentarse o citarse en la sección de "Metodología" del dashboard para demostrar el rigor en la obtención de datos.

---

## 5. Resumen de Hallazgos Clave Sugeridos
> [!IMPORTANT]
> - **El 80%** de la protección forestal en Michoacán ocurre sin apoyo económico externo.
> - **Michoacán produce el 75%** del aguacate nacional, concentrando la crisis en un solo estado.
> - **Pino y Encino** son las especies con mayor volumen de extracción y, por ende, las que más pierden terreno ante el monocultivo.

---
**Preparado por**: Antigravity - Senior Data Engineer | Especialista en Bioinformática.
**Estatus**: Datos listos para visualización narrativa.
