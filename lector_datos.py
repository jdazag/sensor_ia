import pandas as pd

def leer_csv(ruta_csv):
    try:
        df = pd.read_csv(ruta_csv)
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Error al leer archivo CSV: {e}")
        return []
