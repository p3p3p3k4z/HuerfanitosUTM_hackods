# 📖 Diccionario de Datos: Dataset Maestro ODS 15 (Michoacán)

Este documento detalla la estructura, fuentes y metodología detrás del dataset unificado para el análisis del impacto ambiental del monocultivo de aguacate en Michoacán, desarrollado para el **HackODS UNAM 2026**.

## 📊 Descripción General
El dataset consolidado se encuentra en: `data/procesados/dataset_maestro_ods15.csv`
- **Granularidad**: Municipal (113 registros).
- **Entidad**: Michoacán de Ocampo (Clave 16).
- **Año Base**: 2022 (Censo Agropecuario).

---

## 📂 Diccionario de Columnas

### Identificación Territorial
| Columna | Descripción |
| :--- | :--- |
| `municipio` | Nombre normalizado del municipio en Michoacán. |

### Métricas de Superficie (Hectáreas - ha)
| Columna | Descripción |
| :--- | :--- |
| `ha_agricola_total` | Superficie total con vocación o uso agrícola (Censo 2022). |
| `ha_forestal_total` | Superficie forestal (Bosque/Selva) cartografiada en el municipio. |
| `ha_urbana` | Superficie de asentamientos humanos y zonas urbanas. |
| `ha_aguacate` | Superficie sembrada específicamente con Aguacate en 2022. |

### Producción Agrícola
| Columna | Descripción |
| :--- | :--- |
| `ton_aguacate` | Producción anual de aguacate en toneladas métricas. |

### Análisis Ambiental y Storytelling
| Columna | Descripción |
| :--- | :--- |
| `pct_bosque` | Ratio de cobertura forestal (`ha_forestal_total` / Superficie Total). |
| `pct_aguacate_en_agri` | % de la tierra agrícola ocupada por aguacate. Indicador de monocultivo. |
| `fase_narrativa` | Etiqueta basada en la Pirámide de Freytag para la narrativa del dashboard. |
| `impact_ratio` | Ratio de presión sobre el suelo (`ha_aguacate` / `ha_agricola_total`). |

### Baselines (Contexto Global/Estatal)
| Columna | Descripción |
| :--- | :--- |
| `baseline_def_nacional` | Tasa de deforestación bruta nacional en 2022 (Fuente: Agenda 2030). |
| `state_reforestacion_total`| Superficie total reforestada en Michoacán en 2022. |
| `state_unidades_forestales`| Número de unidades de producción forestal activas en el estado. |

---

## 🛠 Metodología

### 1. Cálculo de Fases Narrativas
Para facilitar el *storytelling*, los municipios se clasifican automáticamente:
- **Clímax**: Municipios con >5,000 ha de aguacate. Representan el punto álgido del desarrollo económico y la tensión ambiental.
- **Conflicto**: Municipios donde el aguacate ocupa >30% de la tierra agrícola. Zonas de transición y posible deforestación activa.
- **Introducción**: Municipios donde la superficie forestal aún supera a la agrícola.
- **Resolución**: Zonas con baja presencia de monocultivo o en equilibrio.

### 2. Detección de Anomalías (Cambio de Uso de Suelo)
Si el `impact_ratio` es mayor a 1.0, indica que la superficie sembrada de aguacate excede la superficie agrícola cartografiada de forma oficial. Esto es un fuerte indicador de **aguacate sembrado en terrenos forestales no registrados para uso agrícola**.

---

## 📚 Fuentes de Datos
1.  **INEGI - Censo Agropecuario 2022**: Datos de producción, cultivos y superficies municipales.
2.  **Agenda 2030**: Indicadores ODS 15 (Deforestación Bruta y Proporción Forestal Nacional).
3.  **Registro Agrario Nacional / Censo Forestal**: Estadísticas estatales de unidades de producción y reforestación.

---
> [!TIP]
> **Uso Sugerido**: Este dataset está optimizado para su uso en **Plotly (Python)** y **Quarto (.qmd)**. Consulte el script `etl_maestro_ods15.py` para regenerar los datos en caso de cambios en las fuentes crudas.
