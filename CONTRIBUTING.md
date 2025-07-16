# Guía para contribuir al proyecto `sensor_ia`

¡Gracias por tu interés en contribuir a este proyecto! Sigue estas instrucciones para mantener una colaboración organizada y efectiva.

## 📦 Clona el repositorio

```bash
git clone https://github.com/jdazag/sensor_ia.git
cd sensor_ia
```

## 🛠️ Crea una rama para tu contribución

```bash
git checkout develop
git pull
git checkout -b feature/nombre-descriptivo
```

Ejemplos:
- `feature/carga-csv-rapida`
- `bugfix/error-tiempo-espera`
- `hotfix/reparacion-produccion`

## 🧪 Ejecuta pruebas localmente

Asegúrate de que tu código no rompe la funcionalidad existente. Usa:

```bash
python main.py
```

o si es FastAPI:

```bash
uvicorn main_api:app --reload
```

## 🧹 Estilo y convenciones

- Sigue el estilo PEP8 para Python
- Usa nombres descriptivos para funciones y variables
- Escribe comentarios claros cuando sea necesario
- Usa `snake_case` para Python

## ✅ Commits claros

Utiliza el formato convencional de commits:

- `feat:` para nuevas funciones
- `fix:` para correcciones de bugs
- `docs:` para cambios en la documentación
- `refactor:` para cambios internos sin nueva funcionalidad
- `test:` para añadir o mejorar pruebas
- `chore:` para otros cambios menores

Ejemplo:

```bash
git commit -m "feat: añade validación para datos incompletos"
```

## 🔁 Solicita un Pull Request

Una vez termines tu desarrollo:

1. Sube tus cambios:
```bash
git push origin feature/nombre-descriptivo
```

2. Crea un Pull Request hacia `develop` desde GitHub
3. Agrega una breve descripción de los cambios

Gracias por tu colaboración 🚀
