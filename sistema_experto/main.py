from knowledge.rules import rules
from knowledge.senderos_data import senderos
from knowledge.pesca_data import pesca_lugares
from knowledge.museos_data import museos
from knowledge.deportes_invierno_data import deportes_invierno
from engine.inference import infer_conclusion

def selector_actividad():
    print("\n🎯 Bienvenido al Sistema Experto de Turismo Fueguino")
    print("¿Qué tipo de actividad estás buscando?")
    print("1) Senderismo")
    print("2) Paisajismo y Naturaleza")
    print("3) Cultura")
    print("4) Pesca deportiva")
    print("5) Deportes de invierno")
    opcion = input("Seleccioná una opción (1 a 5): ").strip()
    return opcion

def flujo_senderismo():
    dificultad = input("Elegí dificultad (Baja / Media / Alta / Todas): ").capitalize()
    estacion = input("Estación del año (Verano / Otoño / Invierno / Primavera / Todo el año): ").capitalize()
    ubicacion = input("Ubicación deseada (Ushuaia / Tolhuin / Río Grande / Parque Nacional Tierra del Fuego / Todas): ").title()

    hechos = {
        "difficulty": dificultad,
        "season": estacion,
        "location": ubicacion,
        "motivation": "Ejercicio"
    }

    conclusiones = infer_conclusion(rules, hechos)
    mostrar_resultado(conclusiones)
    mostrar_senderos("Ejercicio", ubicacion, dificultad)

def flujo_naturaleza():
    ubicacion = input("Ubicación (Ushuaia / Tolhuin / Río Grande / Todas): ").title()
    mostrar_senderos("Naturaleza", ubicacion, "Baja")

def flujo_cultura():
    ubicacion = input("Ubicación (Ushuaia / Río Grande / Tolhuin / Todas): ").title()
    hechos = {
        "location": ubicacion,
        "motivation": "Cultura"
    }
    conclusiones = infer_conclusion(rules, hechos)
    mostrar_resultado(conclusiones)
    mostrar_museos(ubicacion)

def flujo_pesca():
    ubicacion = input("Ubicación (Río Grande / Tolhuin / Ushuaia / Todas): ").title()
    estacion = input("Estación del año (Verano / Otoño / Invierno / Primavera / Todo el año): ").capitalize()
    hechos = {
        "location": ubicacion,
        "season": estacion,
        "motivation": "Pesca"
    }
    conclusiones = infer_conclusion(rules, hechos)
    mostrar_resultado(conclusiones)
    mostrar_pesca(ubicacion)

def flujo_invierno():
    ubicacion = input("Ubicación (Ushuaia / Ruta 3 / Todas): ").title()
    hechos = {
        "location": ubicacion,
        "season": "Invierno",
        "motivation": "Aventura"
    }
    conclusiones = infer_conclusion(rules, hechos)
    mostrar_resultado(conclusiones)
    mostrar_deportes_invierno(hechos)

# Funciones auxiliares (igual que antes pero con nuevos parámetros)

def mostrar_resultado(conclusiones):
    if not conclusiones:
        print("\n⚠️ No se encontraron conclusiones razonadas para esta combinación.\n")
    else:
        print("\n✅ Recomendaciones del sistema experto:\n")
        for c in conclusiones:
            print(f"🔹 Regla {c['rule_id']}: {c['conclusion']}")
            print(f"   👉 {c['explanation']}\n")

def mostrar_senderos(motivacion, ubicacion, dificultad="Todas"):
    rutas = [
        s for s in senderos
        if motivacion in s["motivation_tags"]
        and (ubicacion == "Todas" or s["location"] == ubicacion)
        and (dificultad == "Todas" or s["difficulty"] == dificultad)
    ]
    if rutas:
        print("🥾 Senderos recomendados:\n")
        for s in rutas:
            print(f"🔸 {s['name']} – {s['location']} – Dificultad: {s['difficulty']}")
            print(f"   ⏱️ Duración estimada: {s['duration']}")
            print(f"   📍 GPX: {s['gpx_url']}\n")
    else:
        print("❌ No se encontraron senderos que coincidan con los criterios.\n")

def mostrar_pesca(ubicacion):
    puntos = [
        p for p in pesca_lugares
        if ubicacion == "Todas" or ubicacion in p["notes"] or ubicacion in p["name"]
    ]
    if puntos:
        print("🎣 Sitios sugeridos para pesca:\n")
        for p in puntos:
            print(f"🎯 {p['name']} – Tipo: {p['location_type']}")
            print(f"   🐟 Especies: {', '.join(p['species'])}")
            print(f"   📆 Temporada: {p['season']}")
            print(f"   📝 Info: {p['notes']}\n")
    else:
        print("❌ No se encontraron sitios de pesca compatibles.\n")

def mostrar_museos(ubicacion):
    relevantes = [
        m for m in museos if ubicacion == "Todas" or m["location"] == ubicacion
    ]
    if relevantes:
        print("🏛️ Museos recomendados:\n")
        for m in relevantes:
            print(f"🏺 {m['name']} – {m['theme']}")
            print(f"   🕑 Horarios: {m['hours']} – 📆 Temporada: {m['season']}")
            print(f"   📍 Ubicación: {m['location']}")
            print(f"   📝 {m['notes']}\n")
    else:
        print("❌ No se encontraron museos en esa ubicación.\n")

def mostrar_deportes_invierno(hechos):
    actividades = [
        c for c in deportes_invierno
        if (hechos["location"] == "Todas" or hechos["location"] in c["location"])
        and hechos["season"] in c["season"]
    ]
    if actividades:
        print("⛷️ Actividades de invierno recomendadas:\n")
        for c in actividades:
            print(f"❄️ {c['name']} – {', '.join(c['activities'])}")
            print(f"   📍 Ubicación: {c['location']} – 🏅 Nivel: {c['level']}")
            print(f"   📆 Temporada: {c['season']}")
            print(f"   📝 Info: {c['notes']}\n")
    else:
        print("❌ No se encontraron actividades invernales compatibles.\n")

# Punto de entrada principal

if __name__ == "__main__":
    opcion = selector_actividad()

    if opcion == "1":
        flujo_senderismo()
    elif opcion == "2":
        flujo_naturaleza()
    elif opcion == "3":
        flujo_cultura()
    elif opcion == "4":
        flujo_pesca()
    elif opcion == "5":
        flujo_invierno()
    else:
        print("❌ Opción no válida. Reiniciá el sistema e ingresá un número del 1 al 5.")
