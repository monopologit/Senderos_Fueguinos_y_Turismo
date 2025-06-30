<p align="center">
  <img src="web_app/static/Logo_fueguino.png" alt="Logo Fueguino" width="240"/>
</p>

<h1 align="center">Sistema Experto de Senderismo y Turismo Fueguino</h1>
<p align="center"><em>Una aventura lógica en el fin del mundo</em></p>

---

### 🎓 Proyecto académico

- **Materia:** Desarrollo de Sistemas de Inteligencia Artificial  
- **Profesor:** Lic. Martín Mirabete  
- **Carrera:** Ciencia de Datos e Inteligencia Artificial  
- **Instituto:** Politécnico Malvinas Argentinas – Río Grande, Tierra del Fuego  
- **Alumno:** Carlos Alberto Gongora  

---

### 🧠 ¿Qué es un sistema experto?

Un **sistema experto** es un programa que simula el razonamiento de una persona especialista en un área concreta. Utiliza hechos, reglas y deducción lógica para emitir recomendaciones o resolver problemas.

Sus componentes fundamentales son:

- **Base de conocimientos:** reglas y hechos que representan el saber experto  
- **Motor de inferencia:** mecanismo que evalúa las reglas y activa conclusiones  
- **Justificación lógica:** explica por qué se llegó a determinada respuesta  
- **Interfaz de usuario:** punto de interacción para introducir datos y obtener resultados  

---

### 🧩 ¿En qué se basa este sistema experto fueguino?

Este proyecto fue desarrollado con enfoque territorial, educativo y lógico. Su funcionamiento se apoya en:

- ✅ Reglas explícitas en código Python, construidas manualmente  
- ✅ Separación entre hechos (respuestas del usuario) y conocimiento (reglas)  
- ✅ Evaluación condicional por estación, motivación, dificultad, localidad  
- ✅ Motor de inferencia artesanal que explica sus conclusiones  
- ✅ Modularidad que permite extender el sistema a nuevos dominios  

---

### 🧱 Arquitectura general del sistema

[ Usuario ]

    │ 

    ▼ 

[ Interfaz web Flask ] 

    │ 

    ▼ 

[ Adaptador de hechos ] → Traduce respuestas en hechos lógicos 

    │ 

    ▼ 

[ Motor de inferencia ] 

    │ 

    ├─▶ Evalúa reglas (senderos, pesca, cultura, imagen) 

    └─▶ Devuelve recomendaciones y justificación 

    ▼ 

[ Respuesta web o PDF interpretativo ]


---

### ✨ Funcionalidades principales

- Recomendaciones personalizadas según estación, región, dificultad y motivación  
- Justificación de cada sugerencia con reglas activadas visibles para el usuario  
- Exportación en PDF para la actividad “Imagen (Flora y Fauna)”  
- Interfaz web compatible con dispositivos móviles  
- Información contextual sobre flora, fauna y actividades fueguinas  

---

### 🌍 Dominios implementados

- **Senderismo**: senderos por dificultad, estación y motivación “Ejercicio”  
- **Imagen (Flora y Fauna)**: recorridos interpretativos por motivación “Naturaleza”  
- **Cultura**: museos por localidad y enfoque temático  
- **Pesca**: zonas y especies disponibles según época del año  
- **Invierno**: deportes estacionales como esquí, snowboard, patinaje  

---

### 🖨 Exportación PDF interpretativa

Desde el dominio “Imagen”, el sistema genera una ficha con:

- Flora típica (lenga, notro, coirón)  
- Fauna fueguina (zorros, cauquenes, carpinteros)  
- Especie invasora: castor canadiense  
- Encabezado visual con logo y pie de página educativo  

---

### 💻 Instalación y ejecución local

#### Requisitos

- Python 3.11+  
- pip  
- Navegador web moderno  
- Git (opcional)

#### Instrucciones

```bash
# Clonar el repositorio
git clone https://github.com/monopologit/Senderos_Fueguinos_y_Turismo.git
cd Senderos_Fueguinos_y_Turismo

# Crear entorno virtual (opcional)
python -m venv .venv
.venv\Scripts\activate           # en Windows
source .venv/bin/activate       # en Linux/macOS

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor Flask
set FLASK_APP=web_app/app.py     # en Windows
flask run
# o
export FLASK_APP=web_app/app.py  # en Linux/macOS
flask run

Una vez iniciado, accedé a: http://127.0.0.1:5000

### Acceso desde celular (en red local)

1) Buscá tu IP local con ipconfig (Windows) o ifconfig (Linux/macOS)

2) Ejecutá el servidor así:

```bash
    flask run --host=0.0.0.0

3) Ingresá desde el navegador del celular:

http://TU_IP_LOCAL:5000

(ambos dispositivos deben estar conectados a la misma red Wi-Fi)

### Estructura del repositorio

SENDEROS_FUEGUINOS_Y_TURISMO/

├── sistema_experto/              ← Motor de inferencia y reglas

├── web_app/

│   ├── static/                   ← Logo, CSS

│   ├── templates/                ← HTML + plantilla PDF

│   └── app.py                    ← Punto de entrada Flask

├── tracks/                       ← Archivos GPX de senderos

├── docs/                         ← Documentación técnica

├── requirements.txt

└── README.md

### Licencia y versión

- Versión: v1.0.0

- Licencia: MIT (puede agregarse el archivo LICENSE si se desea publicar abiertamente)

### Autor

Carlos Alberto Gongora Explorador de ideas estructuradas con lógica. Desarrollado en Tierra del Fuego, al sur del sur.
