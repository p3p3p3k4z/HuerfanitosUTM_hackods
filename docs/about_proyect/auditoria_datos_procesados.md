# Auditoría de Datos Procesados y Análisis de Problemática (ODS 15)

Este documento contiene la estructura (columnas/atributos) de cada archivo CSV encontrado en el directorio `data/procesados`, junto con un análisis de su utilidad y la problemática que reflejan en el contexto de la deforestación y el cultivo de aguacate en Michoacán.

### `data/procesados/biodiversidad_especies_ods15.csv`
**Atributos:**
- `entidad`
- `Encino`
- `Otras`
- `Pino`

**Utilidad y Problemática Reflejada:**
Sirve para analizar la composición forestal por estado. En el contexto de Michoacán, refleja qué especies maderables (pinos y encinos) dominan los ecosistemas que están bajo mayor presión por el cambio de uso de suelo. La tala clandestina o quema inducida suele afectar directamente a estas especies para dar paso a las huertas de aguacate.

---

### `data/procesados/contexto_nacional_ods15.csv`
**Atributos:**
- `ENT_FED`
- `ha_agricola_total`
- `ha_forestal_total`
- `ha_aguacate`
- `ton_aguacate`
- `cuota_produccion_nacional`
- `indice_presion_forestal`

**Utilidad y Problemática Reflejada:**
Proporciona el panorama macro a nivel estatal. El `indice_presion_forestal` y la `cuota_produccion_nacional` son claves para demostrar cómo la alta rentabilidad y volumen del aguacate (`ton_aguacate`) ejercen presión sobre las zonas forestales (`ha_forestal_total`). Refleja la problemática central: el éxito agrícola está inversamente correlacionado con la conservación forestal en estados líderes.

---

### `data/procesados/dataset_maestro_ods15.csv`
**Atributos:**
- `municipio`
- `ha_agricola_total`
- `ha_forestal_total`
- `ha_urbana`
- `ha_aguacate`
- `ton_aguacate`
- `pct_bosque`
- `pct_aguacate_en_agri`
- `fase_narrativa`
- `baseline_def_nacional`
- `state_reforestacion_total`
- `state_unidades_forestales`
- `impact_ratio`

**Utilidad y Problemática Reflejada:**
Es el corazón de la visualización y análisis. Permite cruzar el porcentaje de territorio dedicado al aguacate (`pct_aguacate_en_agri`) con el ratio de impacto ambiental (`impact_ratio`) a nivel municipal. Refleja qué municipios específicos (ej. Uruapan, Tancítaro) son "focos rojos" donde la expansión aguacatera está consumiendo la cubierta arbórea (`pct_bosque`).

---

### `data/procesados/gestion_ambiental_ods15.csv`
**Atributos:**
- `entidad`
- `total_unidades`
- `unidades_con_acciones`
- `unidades_con_apoyo`
- `unidades_sin_apoyo`
- `pct_acciones_sin_apoyo`

**Utilidad y Problemática Reflejada:**
Muestra las respuestas institucionales e independientes ante la crisis. Un alto `pct_acciones_sin_apoyo` indica que los productores o comunidades están tomando medidas de conservación por cuenta propia, revelando posibles deficiencias, falta de presupuesto o ineficiencia en las políticas públicas de subsidio forestal.

---

### `data/procesados/gfw_clases_bosque_natural.csv`
**Atributos:**
- `iso`
- `adm1` (Estado)
- `sbtn_natural_forests__class`
- `area__ha`

**Utilidad y Problemática Reflejada:**
Clasifica las áreas de bosque natural. Útil para distinguir qué calidad de bosque se está perdiendo (primario, secundario, etc.). Permite focalizar la narrativa en la pérdida de ecosistemas irremplazables frente a zonas de menor densidad o regeneradas.

---

### `data/procesados/gfw_cobertura_municipal_2010.csv`
**Atributos:**
- `iso`
- `adm1`
- `adm2` (Municipio)
- `umd_tree_cover_extent_2010__ha`
- `area__ha`
- `municipio`

**Utilidad y Problemática Reflejada:**
Establece la "línea base" (año 2010) de cobertura arbórea por municipio. Sirve como punto de partida para calcular todo el bosque que se ha deforestado en la última década debido al "oro verde".

---

### `data/procesados/gfw_drivers_perdida_completo.csv`
**Atributos:**
- `drivers_type`
- `loss_year`
- `loss_area_ha`
- `gross_carbon_emissions_Mg`

**Utilidad y Problemática Reflejada:**
Asigna causas a la deforestación (ej. agricultura, incendios, tala). Relaciona directamente la pérdida de hectáreas con emisiones de carbono. Es fundamental para demostrar empíricamente que la agricultura (y específicamente los cultivos de alto valor) es el motor principal del cambio climático local y la pérdida de hábitat.

---

### `data/procesados/gfw_historico_agricola_mich.csv`
**Atributos:**
- `loss_year`
- `loss_area_ha`

**Utilidad y Problemática Reflejada:**
Muestra una serie de tiempo directa de cuántas hectáreas se pierden anualmente por expansión agrícola en Michoacán. Refleja la tendencia histórica: si las hectáreas perdidas aumentan a la par que el boom del precio del aguacate.

---

### `data/procesados/gfw_historico_perdida_emisiones.csv` y `gfw_perdida_bosque_primario.csv`
**Atributos:**
- `iso`
- `adm1`
- `umd_tree_cover_loss__year`
- `umd_tree_cover_loss__ha`
- `gfw_gross_emissions_co2e_all_gases__Mg`

**Utilidad y Problemática Reflejada:**
Cruza la pérdida de cobertura y de bosque primario (el más valioso biológicamente) con las toneladas de gases de efecto invernadero emitidas. Subraya la problemática global del ODS 15 y el ODS 13 (Acción por el clima): perder bosques primarios libera reservas de carbono milenarias, exacerbando el calentamiento global.

---

### `data/procesados/gfw_historico_primario_mich.csv`
**Atributos:**
- `anio`
- `ha_perdida_primaria`

**Utilidad y Problemática Reflejada:**
Una versión simplificada de la pérdida de bosque primario. Excelente para crear un gráfico de barras o líneas simple que alarme visualmente sobre la destrucción anual de los ecosistemas más prístinos y sensibles de la entidad.

---

### `data/procesados/gfw_municipal_baselines.csv`
**Atributos:**
- `municipio`
- `ha_cobertura_2010`
- `ha_total_municipio`

**Utilidad y Problemática Reflejada:**
Sirve para calcular porcentajes relativos de pérdida (qué proporción de la cobertura original de 2010 o de su territorio total ya no existe). Permite comparar justamente municipios grandes contra pequeños.
