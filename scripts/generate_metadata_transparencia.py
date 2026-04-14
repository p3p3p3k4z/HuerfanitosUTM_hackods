# /// script
# dependencies = [
#     "pandas",
# ]
# ///

"""
Metadata Generator for ODS 15 - HackODS UNAM 2026.
Focus: Transparency and data sourcing for judges and researchers.
Author: Antigravity (Senior Data Engineer)
"""

import json
import os
import logging

# Paths
PROCESSED_DATA_PATH = "data/procesados"
OUTPUT_FILE = os.path.join(PROCESSED_DATA_PATH, "transparencia_fuentes_ods15.json")

def generate_metadata():
    metadata = {
        "project": "HackODS UNAM 2026 - ODS 15 Michoacán",
        "description": "Repositorio de datos procesados para el análisis del impacto del aguacate.",
        "last_updated": "2026-04-14",
        "sources": [
            {
                "id": "INEGI_CA_2022",
                "name": "Censo Agropecuario 2022",
                "files": ["ca_2022_upagro_csv.zip", "ca_2022_superficie_csv.zip"],
                "variables": ["Superficie Sembrada", "Toneladas Producidas", "Superficie Forestal", "Superficie Agrícola"],
                "resolution": "Nacional, Estatal, Municipal"
            },
            {
                "id": "CONAFOR_ESTADISTICA",
                "name": "Estadística Forestal (Varios)",
                "files": ["especies_arboles.xlsx", "proteccion_ambiental.xlsx", "produccion_forestal.xlsx"],
                "variables": ["Volumen por especie", "Acciones de protección", "Apoyos económicos"],
                "resolution": "Estatal"
            },
            {
                "id": "AGENDA_2030_MX",
                "name": "Indicadores ODS México",
                "files": ["15.1.1_dc_450_es.csv", "15n.2.1_sh_es.csv"],
                "variables": ["Tasa de deforestación bruta", "Proporción de superficie forestal"],
                "resolution": "Nacional"
            }
        ],
        "methodology": {
            "impact_ratio": "ha_aguacate / ha_agricola_cartografiada (Indicador de invasión forestal)",
            "protection_gap": "unidades_con_acciones - unidades_con_apoyo",
            "narrative_phases": "Clasificación basada en Dominancia vs Reserva (Clímax, Conflicto, Introducción)"
        }
    }

    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding='utf-8') as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)
    
    print(f"Metadata generada exitosamente en: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_metadata()
