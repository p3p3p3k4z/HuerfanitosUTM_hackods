# /// script
# dependencies = [
#     "pandas",
# ]
# ///

"""
National Context ETL for ODS 15 - HackODS UNAM 2026.
Focus: Comparing avocado production dominance and forest pressure across Mexican states.
Author: Antigravity (Senior Data Engineer)
"""

import os
import zipfile
import pandas as pd
import logging
from typing import Dict

# Paths
RAW_DATA_PATH = "data/crudos"
PROCESSED_DATA_PATH = "data/procesados"
OUTPUT_FILE = os.path.join(PROCESSED_DATA_PATH, "contexto_nacional_ods15.csv")

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )
    return logging.getLogger("ETL_Nacional")

class ETLNacional:
    def __init__(self):
        self.logger = setup_logging()
        os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

    def _read_csv_from_zip(self, zip_path: str, csv_name: str) -> pd.DataFrame:
        full_path = os.path.join(RAW_DATA_PATH, zip_path)
        try:
            with zipfile.ZipFile(full_path, 'r') as z:
                with z.open(csv_name) as f:
                    return pd.read_csv(f, low_memory=False)
        except Exception as e:
            self.logger.error(f"Error leyendo {csv_name} en {zip_path}: {e}")
            return pd.DataFrame()

    def process_data(self):
        self.logger.info("Iniciando extracción de contexto nacional...")
        
        # 1. Avocado Production
        df_prod = self._read_csv_from_zip("ca_2022_upagro_csv.zip", "conjunto_datos/ca2022_agr01.csv")
        if df_prod.empty: return

        # filter for Avocado and Group by State
        df_avo = df_prod[df_prod['CULTIVO'].str.contains('Aguacate', case=False, na=False)].copy()
        state_avo = df_avo.groupby('ENT_FED').agg({
            'SUPSEM_AGCA': 'sum',
            'TON_AGCA': 'sum'
        }).reset_index()
        state_avo = state_avo.rename(columns={'SUPSEM_AGCA': 'ha_aguacate', 'TON_AGCA': 'ton_aguacate'})

        # 2. Forest Surface
        df_surf = self._read_csv_from_zip("ca_2022_superficie_csv.zip", "conjunto_datos/ca2022_01.csv")
        if df_surf.empty: return

        state_surf = df_surf.groupby('ENT_FED').agg({
            'SUP_CARTOG_AG': 'sum',
            'SUP_CARTOG_FO': 'sum'
        }).reset_index()
        state_surf = state_surf.rename(columns={'SUP_CARTOG_AG': 'ha_agricola_total', 'SUP_CARTOG_FO': 'ha_forestal_total'})

        # 3. Merge
        self.logger.info("Unificando datos estatales...")
        master = pd.merge(state_surf, state_avo, on='ENT_FED', how='left').fillna(0)

        # 4. Analytics
        # Michoacan dominance %
        total_ton = master[master['ENT_FED'] == '00 NAL']['ton_aguacate'].values[0]
        if total_ton == 0: total_ton = master['ton_aguacate'].sum() / 2 # Backup if 00 NAL missing
        
        master['cuota_produccion_nacional'] = master['ton_aguacate'] / total_ton
        
        # Pressure Index
        master['indice_presion_forestal'] = master['ha_aguacate'] / (master['ha_forestal_total'] + 1)
        
        # Sort and Save (Exclude 00 NAL for the table but keep it for calculations if needed)
        # Usually for charts we want the states only
        master_states = master[master['ENT_FED'] != '00 NAL'].sort_values(by='ton_aguacate', ascending=False)
        
        master_states.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')
        self.logger.info(f"Archivo generado: {OUTPUT_FILE}")
        self.logger.info(f"Top productor: {master_states.iloc[0]['ENT_FED']} con {master_states.iloc[0]['ton_aguacate']:.2f} toneladas.")

if __name__ == "__main__":
    ETLNacional().process_data()
