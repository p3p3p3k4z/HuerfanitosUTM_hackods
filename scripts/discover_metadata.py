import os
import pandas as pd
import zipfile
import io

def get_file_metadata(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    metadata = {
        "filename": os.path.basename(filepath),
        "path": filepath,
        "type": "Unknown",
        "years": [],
        "region": "Unknown",
        "variables": []
    }
    
    try:
        if ext == ".csv":
            df = pd.read_csv(filepath, nrows=5)
            metadata["type"] = "CSV"
            metadata["variables"] = list(df.columns)
            # Try to find years in columns or data
            if "anio" in df.columns or "año" in df.columns:
                df_full = pd.read_csv(filepath, usecols=[c for c in df.columns if "año" in c.lower() or "anio" in c.lower()])
                metadata["years"] = sorted(df_full.iloc[:, 0].unique().tolist())
        
        elif ext in [".xls", ".xlsx"]:
            df = pd.read_excel(filepath, nrows=5)
            metadata["type"] = "Excel"
            metadata["variables"] = list(df.columns)
            
        elif ext == ".zip":
            metadata["type"] = "ZIP"
            with zipfile.ZipFile(filepath, 'r') as z:
                metadata["variables"] = [f.filename for f in z.infolist()]
                # If there's a dictionary or small CSV, try to peek
                for f in z.namelist():
                    if "diccionario" in f.lower() and f.endswith(".csv"):
                        with z.open(f) as cf:
                            df = pd.read_csv(cf, nrows=5)
                            metadata["variables"].append(f"Header in {f}: {list(df.columns)}")
                            
    except Exception as e:
        metadata["error"] = str(e)
        
    return metadata

def scan_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith("."): continue
            res = get_file_metadata(os.path.join(root, file))
            results.append(res)
    return results

if __name__ == "__main__":
    crudos_path = "data/crudos"
    print(f"Scanning {crudos_path}...")
    metadata_list = scan_directory(crudos_path)
    
    # Generate a simple markdown table summary
    print("\n### Auditoría de Metadatos\n")
    print("| Conjunto de Datos | Tipo | Temporalidad | Variables Clave |")
    print("|---|-|---|---|")
    for m in metadata_list:
        years_str = ", ".join(map(str, m.get("years", [])))[:30]
        vars_str = ", ".join(m.get("variables", []))[:50] + "..."
        print(f"| {m['filename']} | {m['type']} | {years_str} | {vars_str} |")
