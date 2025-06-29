Sistema Experto de Senderismo y Turismo Fueguino

Una aventura lógica en el fin del mundo

Este sistema experto es una aplicación web desarrollada con Flask que brinda recomendaciones personalizadas para actividades turísticas en la provincia de Tierra del Fuego, Argentina. A través de reglas lógicas e interpretación ambiental, permite a residentes y visitantes descubrir senderos, museos, sitios de pesca y actividades de invierno con enfoque educativo y territorial.

Características principales

Recomendaciones personalizadas según estación, actividad, ubicación y nivel de dificultad

Motor de inferencia lógico que justifica sus respuestas con reglas activadas y explicaciones

Interfaz web clara, responsiva y accesible desde dispositivos móviles

Información interpretativa sobre flora y fauna fueguina al elegir la actividad “Imagen (Flora y Fauna)”

Generación dinámica de fichas ambientales en PDF

Integración de enlaces GPX y datos temáticos de alto valor regional

Tecnologías utilizadas

Python 3.11+

Flask

HTML + CSS (diseño responsive)

Motor de inferencia artesanal (reglas + hechos)

xhtml2pdf para exportación de PDFs interpretativos

Estructura del repositorio

SENDEROS_FUEGUINOS_Y_TURISMO/

├── .venv/                      # Entorno virtual

├── docs/                      # Documentación técnica

├── sistema_experto/           # Motor de inferencia y base de conocimiento

├── tracks/                    # Archivos GPX y rutas sugeridas

├── web_app/

│   ├── app.py                 # App Flask principal

│   ├── static/

│   │   ├── style.css

│   │   └── logo_fueguino.png

│   └── templates/

│       ├── index.html

│       └── ficha_pdf.html

├── README.md

└── requirements.txt

Dominios implementados

Senderismo: filtros por dificultad, estación y ubicación con motivación “Ejercicio”

Imagen (Flora y Fauna): selección de senderos con motivación “Naturaleza” y bloque interpretativo ambiental

Cultura: museos por localidad, tema y temporada

Pesca: sitios y especies según temporada y ubicación

Invierno: actividades estacionales por nivel y región

Exportación PDF

El sistema permite descargar una ficha interpretativa en PDF desde la actividad “Imagen”, con información de:

Flora típica fueguina

Fauna destacada

Especie invasora (castor canadiense)

Encabezado visual con logo y pie de página explicativo

Instalación y uso local

Requisitos previos

Python 3.11 o superior

Git

Navegador web

Clonación del repositorio

git clone https://github.com/monopologit/Senderos_Fueguinos_y_Turismo.git

cd Senderos_Fueguinos_y_Turismo

Creación del entorno virtual (opcional)

python -m venv .venv

.venv\Scripts\activate           # En Windows

# o

source .venv/bin/activate       # En Linux/macOS

Instalación de dependencias

pip install -r requirements.txt

Ejecución del sistema

set FLASK_APP=web_app/app.py     # En Windows

flask run

# o

export FLASK_APP=web_app/app.py  # En Linux/macOS

flask run

Accedé desde el navegador a: http://127.0.0.1:5000

Autoría

Carlos A. Gongora – Tierra del Fuego, Argentina Explorador de ideas estructuradas 
con corazón lógico y espíritu fueguino.
