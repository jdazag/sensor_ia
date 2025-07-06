from lector_datos import leer_csv
from generador_prompt import generar_prompt
import subprocess

RUTA_CSV = "data/sensores.csv"
MODELO = "mantenimiento"  # Usar el modelo personalizado

def consultar_ollama(prompt):
    try:
        resultado = subprocess.run(
            ["ollama", "run", MODELO],
            input=prompt,
            capture_output=True,
            text=True
        )
        return resultado.stdout.strip()
    except Exception as e:
        return f"Error al consultar Ollama: {e}"

def main():
    datos = leer_csv(RUTA_CSV)
    for entrada in datos:
        prompt = generar_prompt(entrada)
        print("📤 Prompt generado:\n", prompt)
        respuesta = consultar_ollama(prompt)
        print("🛠️ Propuesta de mantenimiento:\n", respuesta)
        print("=" * 60)

if __name__ == "__main__":
    main()
