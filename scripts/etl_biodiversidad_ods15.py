# /// script
# dependencies = [
#     "pandas",
#     "openpyxl",
# ]
# ///

"""
Biodiversity ETL for ODS 15 - HackODS UNAM 2026.
Focus: Tree species production (Pine, Oak) to analyze biological impact.
Author: Antigravity (Senior Data Engineer)
"""

import os
import pandas as pd
import logging
from typing import Dict

# Paths
RAW_DATA_PATH = "data/crudos/forestal"
PROCESSED_DATA_PATH = "data/procesados"
OUTPUT_FILE = os.path.join(PROCESSED_DATA_PATH, "biodiversidad_especies_ods15.csv")

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )
    return logging.getLogger("ETL_Biodiv")

class ETLBiodiversidad:
    def __init__(self):
        self.logger = setup_logging()
        os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

    def process_data(self):
        self.logger.info("Iniciando análisis de biodiversidad maderable...")
        
        path = os.path.join(RAW_DATA_PATH, "especies_arboles.xlsx")
        if not os.path.exists(path):
            self.logger.error(f"Archivo no encontrado: {path}")
            return

        try:
            # Skip headers based on file inspection
            df = pd.read_excel(path, skiprows=5)
            
            # Map columns by position since names are complex
            # 0: Entidad federativa, 1: Especie, 3: Volumen
            df_clean = df.iloc[:, [0, 1, 3]].dropna()
            df_clean.columns = ['entidad', 'especie', 'volumen_madera']
            
            # Filter valid states (removing summaries)
            df_clean = df_clean[df_clean['entidad'].str.contains(r'^\d', na=False)].copy()
            
            # Ensure numeric volume
            df_clean['volumen_madera'] = pd.to_numeric(df_clean['volumen_madera'], errors='coerce').fillna(0)

            # Group by state and species
            self.logger.info("Agregando volúmenes por especie y estado...")
            
            # Species mapping
            def map_main_species(s):
                s = str(s).lower()
                if 'pino' in s: return 'Pino'
                if 'encino' in s: return 'Encino'
                return 'Otras'

            df_clean['especie_grupo'] = df_clean['especie'].apply(map_main_species)
            
            # Pivot table for states
            pivot = df_clean.groupby(['entidad', 'especie_grupo'])['volumen_madera'].sum().unstack(fill_value=0).reset_index()
            
            # Total reforestation/units context would go here if needed, 
            # but we follow "one script per topic".
            
            pivot.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')
            self.logger.info(f"Archivo de biodiversidad generado: {OUTPUT_FILE}")
            
        except Exception as e:
            self.logger.error(f"Error procesando especies: {e}")

if __name__ == "__main__":
    ETLBiodiversidad().process_data()
