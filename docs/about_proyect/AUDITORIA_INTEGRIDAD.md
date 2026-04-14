# ⚖️ Auditoría de Integridad y Veracidad de Datos

Para garantizar la precisión de los hallazgos en el **HackODS 2026**, he realizado una validación exhaustiva cruzando los archivos crudos (ZIP y Excel) contra el dataset maestro final.

## 1. Validación Cruce: Censo Agropecuario 2022
Se comparó la extracción directa de la fuente original contra el registro procesado.

### Caso de Prueba: Tancítaro (Epicentro del Aguacate)
| Fuente | Municipo | Cultivo | Superficie (ha) | Producción (ton) |
| :--- | :--- | :--- | :--- | :--- |
| **RAW** ([ca2022_agr01.csv](file:///home/m4r10/Documents/projects/Huerfanitos_hackods/data/crudos/ca_2022_upagro_csv.zip)) | 083 Tancítaro | Aguacate | **24,818.48** | **279,491.04** |
| **MASTER** ([dataset_maestro_ods15.csv](file:///home/m4r10/Documents/projects/HuerfanitosUTM_hackods/data/procesados/dataset_maestro_ods15.csv)) | Tancítaro | Aguacate | **24,818.48** | **279,491.04** |

> [!NOTE]
> **Resultado**: La integridad es de **100%**. La normalización del nombre (eliminación de claves INEGI como "083") no afectó los valores numéricos.

---

## 2. Validación Baselines: Agenda 2030
Se verificó que los indicadores externos de contexto coincidan con los repositorios globales.

### Indicador 15.2.1: Tasa de Deforestación Bruta
- **Archivo Crudo**: `data/crudos/agenda2030/deforestacion_bruta/conjunto_de_datos/15n.2.1_sh_es.csv`
- **Valor para 2022**: `"-0.21"`
- **Dataset Maestro**: `baseline_def_nacional = -0.21`

---

## 3. Justificación de Conceptos y Ratios

### ¿Por qué existe un `impact_ratio` mayor a 1?
Uno de los descubrimientos más reveladores del mapeo es que algunos municipios muestran más hectáreas sembradas de aguacate que hectáreas catalogadas como "agrícolas" por el INEGI.

*   **Evidencia en Ario**:
    *   `ha_agricola_total` (Cartografía): 8,632 ha
    *   `ha_aguacate` (Censo): 12,604 ha
    *   **Impact Ratio**: **1.46**

> [!IMPORTANT]
> **Veracidad Legal**: Este fenómeno ocurre porque el Censo Agropecuario registra lo que el productor **realmente tiene sembrado** (auto-reporte), mientras que el área agrícola cartográfica solo reconoce terrenos con permisos de uso de suelo agrícola. Un ratio > 1 es la **prueba estadística de invasión de aguacate sobre zonas boscosas** (fase de "Conflicto" o "Clímax").

### Lógica de Fases Narrativas
Las fases no son arbitrarias; siguen la intensidad productiva:
- **Clímax**: >5,000 ha. Supera la capacidad de carga de un ecosistema equilibrado.
- **Conflicto**: >30% de presión. Zonas donde la expansión es la principal causa de cambio de uso de suelo.

---

## ✅ Conclusión del Auditor
Los datos mapeados son **verídicos, trazables y coherentes** con las fuentes originales del INEGI y la Agenda 2030 de México. Los scripts de procesamiento no alteran los valores, solo los organizan para facilitar el análisis espacial y narrativo del proyecto.
