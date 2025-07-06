# 🤖 Sistema de Mantenimiento Predictivo con Ollama

Este proyecto implementa un sistema inteligente que recibe datos de sensores industriales (como temperatura, nivel de fluidos, voltaje y vibración) y genera recomendaciones de mantenimiento utilizando un modelo LLM ejecutado localmente con **Ollama**.

## 🧩 Características principales

- Lectura de datos desde archivos CSV o JSON estructurados
- Generación automática de prompts para diagnóstico
- Modelo Ollama personalizado para mantenimiento industrial
- Posibilidad de expansión a interfaz API o visual

## 📁 Estructura del proyecto
Sensor_IA/
├── data/ # Archivos CSV con datos simulados o reales
├── modelos/ # Modelo Ollama especializado
├── prompts/ # Base de prompts o plantillas
├── lector_datos.py # Módulo para leer archivos de datos
├── generador_prompt.py # Módulo que construye prompts
├── main.py # Script principal para prueba del sistema
├── requirements.txt # Dependencias del proyecto
├── README.md
└── CHANGELOG.md

## 🛠️ Requisitos

- Python 3.9+
- Ollama instalado localmente (https://ollama.com)
- Modelo base (`mistral`, `phi`, etc.)
- pandas

## 🚀 Ejecución

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt

2. Ejecutar el modelo Ollama personalizado:
   ollama create mantenimiento -f modelos/mantenimiento/Modelfile

3. Ejecutar el sistema:
   python main.py

🧠 Entrenamiento personalizado
El modelo personalizado se define en modelos/mantenimiento/Modelfile. Puedes añadir ejemplos en lenguaje natural con etiquetas MESSAGE user / MESSAGE assistant para especializarlo más en el contexto de tus equipos y parámetros reales.

📈 Próximas funcionalidades
* API REST para interacción desde frontend o móvil
* Registro de recomendaciones en historial
* Visualización en dashboard

