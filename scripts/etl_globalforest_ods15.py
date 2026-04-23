"""
ETL Maestro: Global Forest Watch (GFW) - Michoacán
HackODS UNAM 2026 | ODS 15
Este script procesa la TOTALIDAD de los atributos encontrados en la carpeta globalforest:
- Pérdida de cobertura (Ha) y Emisiones (Mg CO2e)
- Clasificación de bosques naturales (SBTN)
- Motores de pérdida (Drivers)
- Cobertura primaria y extensiones municipales
"""

import pandas as pd
import os
import json

RAW_GFW_PATH = "data/crudos/globalforest/"
OUTPUT_PATH = "data/procesados/"
os.makedirs(OUTPUT_PATH, exist_ok=True)

def process_comprehensive_gfw():
    print("INFO: Iniciando procesamiento exhaustivo de atributos GFW...")
    
    # 1. Metadatos Municipales
    path_meta = os.path.join(RAW_GFW_PATH, "Location of tree cover in Michoacán, México/adm2_metadata.csv")
    df_meta = pd.read_csv(path_meta)
    id_to_name = dict(zip(df_meta['adm2__id'], df_meta['name']))
    
    # 2. Clases de Bosque Natural (SBTN)
    path_nat = os.path.join(RAW_GFW_PATH, "Natural forest in Michoacán, México/natural_forest_2020__ha.csv")
    df_nat = pd.read_csv(path_nat)
    # Atributos: sbtn_natural_forests__class, area__ha
    df_nat.to_csv(os.path.join(OUTPUT_PATH, "gfw_clases_bosque_natural.csv"), index=False)
    
    # 3. Cobertura y Extensión Municipal
    path_extent = os.path.join(RAW_GFW_PATH, "Location of tree cover in Michoacán, México/treecover_extent_2010_by_region__ha.csv")
    df_extent = pd.read_csv(path_extent)
    df_extent['municipio'] = df_extent['adm2'].map(id_to_name)
    # Atributos: umd_tree_cover_extent_2010__ha, area__ha
    df_extent.to_csv(os.path.join(OUTPUT_PATH, "gfw_cobertura_municipal_2010.csv"), index=False)
    
    # 4. Pérdida Histórica y Emisiones (ADM1)
    path_loss = os.path.join(RAW_GFW_PATH, "Tree cover loss in Michoacán, México/treecover_loss__ha.csv")
    df_loss = pd.read_csv(path_loss)
    # Atributos: umd_tree_cover_loss__year, umd_tree_cover_loss__ha, gfw_gross_emissions_co2e_all_gases__Mg
    df_loss.to_csv(os.path.join(OUTPUT_PATH, "gfw_historico_perdida_emisiones.csv"), index=False)
    
    # 5. Motores de Pérdida (Drivers) Exhaustivo
    path_drivers = os.path.join(RAW_GFW_PATH, "Tree cover loss by dominant driver in Michoacán, México/tree_cover_loss_by_driver.csv")
    df_drivers = pd.read_csv(path_drivers)
    # Atributos: drivers_type, loss_year, loss_area_ha, gross_carbon_emissions_Mg
    df_drivers.to_csv(os.path.join(OUTPUT_PATH, "gfw_drivers_perdida_completo.csv"), index=False)
    
    # 6. Bosque Primario
    path_primary = os.path.join(RAW_GFW_PATH, "Primary Forest loss in Michoacán, México/treecover_loss_in_primary_forests_2001_tropics_only__ha.csv")
    df_primary = pd.read_csv(path_primary)
    df_primary.to_csv(os.path.join(OUTPUT_PATH, "gfw_perdida_bosque_primario.csv"), index=False)
    
    # Metadatos de Consolidación
    catalog = {
        "datasets": [
            "clases_bosque_natural", "cobertura_municipal", 
            "historico_perdida_emisiones", "drivers_perdida_completo", 
            "perdida_bosque_primario"
        ],
        "variables_totales": [
            "umd_tree_cover_loss__ha", "gfw_gross_emissions_co2e_all_gases__Mg",
            "drivers_type", "sbtn_natural_forests__class", "area__ha"
        ]
    }
    with open(os.path.join(OUTPUT_PATH, "catalogo_gfw_completo.json"), "w") as f:
        json.dump(catalog, f, indent=4)
        
    print("EXITO: Procesamiento de TODOS los atributos de GFW completado.")

if __name__ == "__main__":
    process_comprehensive_gfw()
