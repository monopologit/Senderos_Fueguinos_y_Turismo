import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, render_template, request, send_file
from sistema_experto.knowledge.rules import rules
from sistema_experto.knowledge.senderos_data import senderos
from sistema_experto.knowledge.pesca_data import pesca_lugares
from sistema_experto.knowledge.museos_data import museos
from sistema_experto.knowledge.deportes_invierno_data import deportes_invierno
from sistema_experto.engine.inference import infer_conclusion
from xhtml2pdf import pisa
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    actividades = ["Senderismo", "Imagen", "Cultura", "Pesca", "Invierno"]
    ubicaciones = ["Ushuaia", "Tolhuin", "Río Grande", "Parque Nacional Tierra del Fuego", "Todas"]
    estaciones = ["Verano", "Otoño", "Invierno", "Primavera", "Todo el año"]

    if request.method == "POST":
        actividad = request.form.get("actividad")
        estacion = request.form.get("estacion")
        ubicacion = request.form.get("ubicacion")

        resultados = []
        conclusiones = []
        interpretacion_natural = None

        if actividad == "Senderismo":
            hechos = {
                "difficulty": request.form.get("dificultad"),
                "season": estacion,
                "location": ubicacion,
                "motivation": "Ejercicio"
            }
            conclusiones = infer_conclusion(rules, hechos)
            resultados = [
                s for s in senderos
                if "Ejercicio" in s["motivation_tags"]
                and (ubicacion == "Todas" or s["location"] == ubicacion)
                and (hechos["difficulty"] == "Todas" or s["difficulty"] == hechos["difficulty"])
            ]

        elif actividad == "Imagen":
            hechos = {
                "difficulty": "Baja",
                "season": estacion,
                "location": ubicacion,
                "motivation": "Naturaleza"
            }
            conclusiones = infer_conclusion(rules, hechos)
            resultados = [
                s for s in senderos
                if "Naturaleza" in s["motivation_tags"]
                and s["difficulty"] == "Baja"
                and (ubicacion == "Todas" or s["location"] == ubicacion)
            ]
            interpretacion_natural = interpretacion_natural_fija()

        elif actividad == "Cultura":
            hechos = {
                "season": estacion,
                "location": ubicacion,
                "motivation": "Cultura"
            }
            conclusiones = infer_conclusion(rules, hechos)
            resultados = [
                m for m in museos
                if ubicacion == "Todas" or m["location"] == ubicacion
            ]

        elif actividad == "Pesca":
            hechos = {
                "season": estacion,
                "location": ubicacion,
                "motivation": "Pesca"
            }
            conclusiones = infer_conclusion(rules, hechos)
            resultados = [
                p for p in pesca_lugares
                if ubicacion == "Todas" or ubicacion in p["notes"] or ubicacion in p["name"]
            ]

        elif actividad == "Invierno":
            hechos = {
                "season": "Invierno",
                "location": ubicacion,
                "motivation": "Aventura"
            }
            conclusiones = infer_conclusion(rules, hechos)
            resultados = [
                d for d in deportes_invierno
                if (ubicacion == "Todas" or ubicacion in d["location"])
                and hechos["season"] in d["season"]
            ]

        return render_template(
            "index.html",
            actividades=actividades,
            ubicaciones=ubicaciones,
            estaciones=estaciones,
            actividad_seleccionada=actividad,
            estacion=estacion,
            ubicacion=ubicacion,
            resultados=resultados,
            conclusiones=conclusiones,
            interpretacion_natural=interpretacion_natural
        )

    return render_template("index.html", actividades=actividades, ubicaciones=ubicaciones, estaciones=estaciones)

@app.route("/descargar_pdf")
def descargar_pdf():
    html_renderizado = render_template("ficha_pdf.html", interpretacion=interpretacion_natural_fija())
    resultado_pdf = BytesIO()
    pisa.CreatePDF(html_renderizado, dest=resultado_pdf)
    resultado_pdf.seek(0)
    return send_file(resultado_pdf, as_attachment=True, download_name="ficha_flora_fauna.pdf")

def interpretacion_natural_fija():
    return {
        "flora": [
            "🌳 Lenga (Nothofagus pumilio): árbol dominante de los bosques fueguinos.",
            "🍁 Ñire (Nothofagus antarctica): cambia a tonos naranjas en otoño.",
            "🌿 Canelo: árbol ceremonial mapuche, poco frecuente.",
            "🍓 Frutilla silvestre: visible en claros durante verano."
        ],
        "fauna": [
            "🦊 Zorro colorado fueguino: frecuente en bordes de bosque.",
            "🦅 Cóndor andino: se avista planeando en áreas abiertas.",
            "🪵 Carpintero gigante: de cabeza roja, ícono de los bosques.",
            "🦢 Cauquén común y real: aves migratorias en humedales.",
            "🦙 Guanaco: presente en estepa fueguina."
        ],
        "invasora": "🦫 Castor canadiense: introducido en 1946, modificó humedales y bosques. Hoy es especie invasora monitoreada."
    }
