import pandas as pd
import zipfile
import os
import io

def get_csv_from_zip(zip_path, csv_name):
    if not os.path.exists(zip_path):
        return None
    try:
        with zipfile.ZipFile(zip_path, 'r') as z:
            if csv_name not in z.namelist():
                return None
            with z.open(csv_name) as f:
                return pd.read_csv(f, low_memory=False)
    except Exception as e:
        print(f"Error reading {csv_name} from {zip_path}: {e}")
        return None

def main():
    print("Building Master Dataset ODS 15...")
    output_dir = "data/procesados"
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Aguacate 2022 from Censo Agropecuario
    print("Extracting Aguacate 2022 data...")
    df_agro = get_csv_from_zip("data/crudos/ca_2022_upagro_csv.zip", "conjunto_datos/ca2022_agr01.csv")
    if df_agro is not None:
        # Filter Michoacán (16) and Aguacate
        df_mich_agro = df_agro[df_agro['ENT_FED'].astype(str).str.contains('16', na=False)].copy()
        df_aguacate = df_mich_agro[df_mich_agro['CULTIVO'].astype(str).str.contains('Aguacate', na=False)].copy()
        
        # We want municipality level and state level
        # State level has empty NOM_MUN or it's '16 MIC' summary
        df_aguacate_mun = df_aguacate[df_aguacate['NOM_MUN'].notna() & (df_aguacate['NOM_MUN'] != '')].copy()
        df_aguacate_mun = df_aguacate_mun[['NOM_MUN', 'SUPSEM_AGCA', 'TON_AGCA']].rename(
            columns={'NOM_MUN': 'municipio', 'SUPSEM_AGCA': 'ha_sembrada', 'TON_AGCA': 'ton_produccion'}
        )
        df_aguacate_mun.to_csv(os.path.join(output_dir, "aguacate_mich_municipios_2022.csv"), index=False)
        print(f"Saved {len(df_aguacate_mun)} municipality records.")

    # 2. Forest vs Agri Surface from Censo Forestal 2022
    print("Extracting Forest vs Agri surface comparison...")
    df_for = get_csv_from_zip("data/crudos/ca_2022_upfores_csv.zip", "conjunto_datos/ca2022_for07.csv")
    if df_for is not None:
        # Filter Michoacán
        df_mich_for = df_for[df_for['CVE_ENT'].astype(str).str.contains('16', na=False)].copy()
        # SUP_AGRIC_UPF (Agri in Forest Units), UPF_SUP_BOSQSEL (Forest Area)
        # Note: This is specifically for Forest Management Units (UPF)
        df_mich_for.to_csv(os.path.join(output_dir, "forestal_mich_2022.csv"), index=False)
        print("Saved forestal summary for Michoacán.")

    # 3. Temporal Vegetation Baseline
    print("Processing Vegetation Baseline (2015-2016)...")
    veg_path = "data/crudos/michoacan_vegetacion.csv"
    if os.path.exists(veg_path):
        df_veg = pd.read_csv(veg_path)
        # Aggregate by year and type
        veg_summary = df_veg.groupby(['anio', 'comp']).size().reset_index(name='count')
        veg_summary.to_csv(os.path.join(output_dir, "vegetacion_mich_resumen.csv"), index=False)
        print("Saved vegetation summary.")

    # 4. Master Dataset Construction
    # We will create a state-level time series if possible
    # For now, let's create a 2022 Master for the story Climax
    if df_agro is not None and df_for is not None:
        master_data = {
            'anio': [2022],
            'aguacate_ha': [df_aguacate_mun['ha_sembrada'].sum()],
            'aguacate_ton': [df_aguacate_mun['ton_produccion'].sum()],
            'bosque_ha': [df_mich_for['UPF_SUP_BOSQSEL'].sum()],
            'agri_en_bosque_ha': [df_mich_for['SUP_AGRIC_UPF'].sum()]
        }
        master_df = pd.DataFrame(master_data)
        master_df.to_csv(os.path.join(output_dir, "dataset_maestro_ods15.csv"), index=False)
        print("Master Dataset generated successfully.")

if __name__ == "__main__":
    main()
