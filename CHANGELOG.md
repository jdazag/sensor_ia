---

## ✅ 2. `CHANGELOG.md`

Este archivo te permite llevar un historial de versiones y cambios documentados.

```markdown
# 📋 CHANGELOG

Todas las modificaciones importantes al proyecto se documentan aquí.

---

## [v1.0.0] - 2025-07-05
### Agregado
- Estructura base del proyecto
- Script para leer datos de sensores desde CSV (`lector_datos.py`)
- Generador de prompts a partir de parámetros industriales (`generador_prompt.py`)
- Modelo Ollama personalizado con `Modelfile` para mantenimiento predictivo
- Script principal (`main.py`) que une todo el flujo
- `README.md` y control de versiones con Git

---

## [v1.1.0] - EN DESARROLLO
### Próximos cambios
- Implementación de API REST con FastAPI
- Almacenamiento de resultados en archivo JSON o base de datos
- Comprobación automática de umbrales críticos antes de consultar al modelo
