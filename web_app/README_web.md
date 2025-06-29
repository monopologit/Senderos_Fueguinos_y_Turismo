# 🌍 Interfaz Web – Sistema Experto de Turismo Fueguino

Esta aplicación web con **Flask** ofrece una interfaz interactiva para consultar recomendaciones turísticas de Tierra del Fuego, basadas en un sistema experto modular. El visitante puede seleccionar su actividad, ubicación y estación del año, y recibir recomendaciones justificadas por reglas declarativas.

---

## 🚀 ¿Qué incluye?

- Interfaz HTML con formularios guiados
- Backend Flask que consulta la lógica del sistema experto
- Conclusiones explicadas y senderos filtrados dinámicamente
- Diseño modular y extensible

---

## 🗂️ Estructura del módulo web

web_app/ ├── app.py # Backend principal en Flask ├── templates/ │ └── index.html # Página inicial (formulario + resultados) ├── static/ # (opcional) CSS / imágenes ├── README_web.md 

# Este archivo


> La lógica de inferencia se encuentra en `../sistema_experto/`, integrada como módulo externo

---

## ⚙️ Requisitos

- Python 3.10 o superior
- Flask (`pip install flask` o usar `requirements.txt`)

O instalá directamente:

```bash
pip install -r requirements.txt

