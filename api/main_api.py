from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from generador_prompt import generar_prompt
#import subprocess
import time
import requests

app = FastAPI(title="API de Mantenimiento Predictivo con Ollama")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend en React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de entrada esperada
class SensorData(BaseModel):
    equipo_id: str
    temperatura_aceite: float
    nivel_fluidos: float
    voltaje_bateria: float
    vibracion: float
    timestamp: str

def consultar_ollama(prompt: str) -> str:
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mantenimiento-phi",
                "prompt": prompt,
                "temperature": 0.3,
                "num_predict": 100,
                "stream": False
            },
            headers={
                "Content-Type": "application/json; charset=utf-8"
            },
            timeout=90  # puedes ajustar según el tamaño de tus prompts
        )
        response.raise_for_status()
        result = response.json()
        return result.get("response", "").strip()
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error al consultar Ollama vía API: {e}"
def ping_ollama():
    try:
        r = requests.get("http://localhost:11434")
        return r.status_code == 200
    except:
        return False

@app.get("/precargar-modelo")
def precargar_modelo():
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mantenimiento-phi",
                "prompt": "ping",
                "stream": False
            },
            timeout=90
        )
        result = response.json()
        return {"estado": "Modelo precargado correctamente", "respuesta": result.get("response", "")}
    except Exception as e:
        return {"estado": "Error al precargar modelo", "error": str(e)}

@app.post("/recomendar")
def recomendar_mantenimiento(data: SensorData):
    prompt = generar_prompt(data.dict())
    respuesta = consultar_ollama(prompt)
    return {
        "equipo_id": data.equipo_id,
        "recomendacion": respuesta
    }

from fastapi import File, UploadFile
import pandas as pd
import io

@app.post("/recomendar/lote")
async def recomendar_desde_csv(file: UploadFile = File(...)):
    contenido = await file.read()
    
    try:
        df = pd.read_csv(io.BytesIO(contenido), encoding='utf-8')
    except Exception as e:
        return {"error": f"No se pudo leer el archivo CSV: {e}"}

    # Validar columnas esperadas
    columnas_requeridas = {
        "equipo_id", "timestamp", "temperatura_aceite",
        "nivel_fluidos", "voltaje_bateria", "vibracion"
    }

    if not columnas_requeridas.issubset(set(df.columns)):
        return {
            "error": "El archivo CSV no contiene todas las columnas requeridas: "
                     + ", ".join(columnas_requeridas)
        }

    # Proceder normalmente
    resultados = []
    for _, fila in df.iterrows():
        datos = fila.to_dict()
        try:
            prompt = generar_prompt(datos)
            respuesta = consultar_ollama(prompt)
            resultados.append({
                "equipo_id": datos.get("equipo_id", "desconocido"),
                "timestamp": datos.get("timestamp", ""),
                "recomendacion": respuesta
            })
            time.sleep(0.8)  # ← agregar este delay para que Ollama respire
        except Exception as e:
            if not ping_ollama():
                resultados.append({
                    "equipo_id": datos.get("equipo_id", "desconocido"),
                    "timestamp": datos.get("timestamp", ""),
                    "error": str(e)
                })
                continue
    return JSONResponse(content={"resultados": resultados})
