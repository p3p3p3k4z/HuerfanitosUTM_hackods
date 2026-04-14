# /// script
# dependencies = [
#     "pandas",
#     "openpyxl",
# ]
# ///

"""
Environmental Management ETL for ODS 15 - HackODS UNAM 2026.
Focus: GAP between protection actions and economic support in Michoacán and Mexico.
Author: Antigravity (Senior Data Engineer)
"""

import os
import pandas as pd
import logging

# Paths
RAW_DATA_PATH = "data/crudos/forestal"
PROCESSED_DATA_PATH = "data/procesados"
OUTPUT_FILE = os.path.join(PROCESSED_DATA_PATH, "gestion_ambiental_ods15.csv")

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )
    return logging.getLogger("ETL_Gestion")

class ETLGestion:
    def __init__(self):
        self.logger = setup_logging()
        os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

    def process_data(self):
        self.logger.info("Analizando brecha de gestión y apoyos ambientales...")
        
        path = os.path.join(RAW_DATA_PATH, "proteccion_ambiental.xlsx")
        if not os.path.exists(path):
            self.logger.error(f"Archivo no encontrado: {path}")
            return

        try:
            # Skip headers based on file inspection
            df = pd.read_excel(path, skiprows=5)
            
            # Map columns by position:
            # 0: Entidad, 1: Total Unidades, 2: Unidades con acciones, 3: Unidades con apoyo
            df_slice = df.iloc[:, [0, 1, 2, 3]].dropna()
            df_slice.columns = ['entidad', 'total_unidades', 'unidades_con_acciones', 'unidades_con_apoyo']
            
            # Filter valid states (Exclude National summary and any NaN)
            df_slice = df_slice[~df_slice['entidad'].str.contains('ESTADOS UNIDOS MEXICANOS|Total|Entidad', na=True, case=False)].copy()
            
            # Convert to numeric
            for col in ['total_unidades', 'unidades_con_acciones', 'unidades_con_apoyo']:
                df_slice[col] = pd.to_numeric(df_slice[col], errors='coerce').fillna(0)

            # Calculation of the Protection GAP
            # Ratio of units doing actions without support
            df_slice['unidades_sin_apoyo'] = df_slice['unidades_con_acciones'] - df_slice['unidades_con_apoyo']
            df_slice['pct_acciones_sin_apoyo'] = (df_slice['unidades_sin_apoyo'] / (df_slice['unidades_con_acciones'] + 1)) * 100
            
            df_slice.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')
            self.logger.info(f"Archivo de gestión generado: {OUTPUT_FILE}")
            
            # Specific fact for Michoacan (16)
            mich = df_slice[df_slice['entidad'].str.contains('16', na=False)]
            if not mich.empty:
                gap = mich.iloc[0]['pct_acciones_sin_apoyo']
                self.logger.info(f"Brecha en Michoacán: {gap:.2f}% de las acciones forestales NO tienen apoyo económico.")

        except Exception as e:
            self.logger.error(f"Error procesando gestión: {e}")

if __name__ == "__main__":
    ETLGestion().process_data()
