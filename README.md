# HuerfanitosUTM_Raiz-Data

## Equipo de Trabajo
- **Mario Enrique Ramirez Gallardo**
- **Irving Tristan Perez Zurita**
- **Dante Neil Martinez Jimenez**

## Fuentes de Información
Este proyecto integra datos oficiales para el análisis del ODS 15 (Vida de Ecosistemas Terrestres) en Michoacán:

- **[INEGI - Censo Agropecuario 2022](https://www.inegi.org.mx/)**: Superficie sembrada y producción agrícola-forestal municipal.
- **[CONAFOR - Estadística Forestal](https://snif.cnf.gob.mx/datos-abiertos/)**: Biodiversidad de especies arbóreas y acciones de protección.
- **[Agenda 2030 México - SIODS](https://agenda2030.mx/ODSGoalSelected.html?ti=T&cveArb=ODS0150&goal=0&lang=es#/ind)**: Indicadores de deforestación y cobertura forestal.

<<<<<<< HEAD
Los datos fueron obtenidos de:
[INEGI](https://www.inegi.org.mx/)

=======
Para detalles técnicos adicionales, consulte [transparencia_fuentes_ods15.json](file:///home/m4r10/Documents/projects/HuerfanitosUTM_hackods/data/procesados/transparencia_fuentes_ods15.json).

## ODS Elegidos
- **ODS 15**: Vida de Ecosistemas Terrestres (Meta 15.2 y 15.1).
- **Subtemas**: Deforestación, cambio de uso de suelo, pérdida de biodiversidad (bosques de Pino/Encino).

## Descripción del Proyecto
Este proyecto analiza el impacto ambiental del monocultivo de aguacate en el estado de Michoacán, centrándose en el **ODS 15: Vida de Ecosistemas Terrestres**. A través de un pipeline de datos robusto y una narrativa basada en la pirámide de Freytag, buscamos identificar zonas donde la expansión agrícola está invadiendo áreas forestales protegidas.

## Problema Central (PREGUNTA)
¿En qué medida la expansión del monocultivo de aguacate compromete la integridad de los ecosistemas forestales en Michoacán y el cumplimiento de las metas del ODS 15?

## Coherencia Narrativa
El proyecto estructural el análisis siguiendo la **Pirámide de Freytag**, vinculando los datos con una historia de tensión ambiental:
- **Exposición**: La bonanza del "Oro Verde" y la dominancia de Michoacán en el mercado global.
- **Conflicto**: El cruce de fronteras entre las hectáreas sembradas y la masa forestal remanente.
- **Clímax**: El uso del *Impact Ratio* para detectar invasiones en zonas boscosas (donde la siembra supera la tierra agrícola registrada).
- **Resolución**: Evidencia para la toma de decisiones y visibilización de brechas en apoyos de protección forestal.

## Potencial de Impacto
Este análisis visibiliza el cambio de uso de suelo impulsado por mercados globales, ofreciendo una herramienta de monitoreo para identificar municipios en situación de emergencia climática y fortalecer la protección de los bosques nacionales.

### Justificación ¿Porque esos datos?
Seleccionamos estos datos para evidenciar la tensión entre la expansión del monocultivo de aguacate y la integridad forestal de Michoacán. El contraste entre productividad agrícola y deforestación permite cuantificar la transición de paisajes naturales hacia zonas de explotación intensiva. Esta integración de fuentes ofrece una lectura estadística precisa sobre la presión que enfrenta el ecosistema ante el cambio de uso de suelo.

## Glosario de Indicadores Clave
- **Impact Ratio**: Relación entre superficie de aguacate y frontera agrícola legal; valores mayores a 1.0 sugieren invasión forestal.
- **Cobertura Forestal**: Proporción de bosque nativo remanente por municipio frente a la expansión agrícola.

## Metadatos de los Datos
Para garantizar la transparencia y trazabilidad de la información procesada, se detallan los metadatos de las fuentes oficiales consultadas:

| Dataset | Fuente | Fecha de Descarga | Licencia | Descripción de Variables |
| :--- | :--- | :--- | :--- | :--- |
| **Censo Agropecuario 2022** | [INEGI](https://www.inegi.org.mx/) | 10/04/2026 | [Libre Uso](https://www.inegi.org.mx/inegi/terminos.html) | Superficie sembrada (ha), Toneladas producidas, Superficie Forestal/Agrícola. |
| **Estadística Forestal** | [CONAFOR](https://snif.cnf.gob.mx/datos-abiertos/) | 10/04/2026 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Volumen por especie (m³), Acciones de protección, Apoyos económicos. |
| **Indicadores ODS México** | [Agenda 2030](https://agenda2030.mx/) | 13/04/2026 | [Datos Abiertos](https://datos.gob.mx/libreusomx) | Tasa de deforestación bruta, Proporción de superficie forestal. |

## Ejecucion
Este proyecto utiliza `uv` para la gestión de dependencias, garantizando reproducibilidad total.

1. **Instalar dependencias**:
   ```bash
   uv sync
   ```
2. **Procesar datos**:
   Los scripts en `scripts/` generan los datasets procesados a partir de los archivos crudos:
   ```bash
   uv run scripts/etl_maestro_ods15.py
   ```
3. **Explorar resultados**:
   Abra el notebook principal para ver el análisis y las visualizaciones:
   ```bash
   uv run jupyter notebook notebooks/blabla.ipynb
   ```
>>>>>>> 0b5f451eb98075114b133cf027be9b46313f7f9e
