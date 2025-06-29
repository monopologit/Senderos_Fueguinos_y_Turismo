# sistema_experto/knowledge/rules.py

rules = [
    {
        "id": "R1",
        "conditions": {
            "difficulty": "Alta",
            "season": "Invierno"
        },
        "conclusion": "No recomendado",
        "explanation": "Evitar senderos de alta dificultad en invierno por riesgo de clima extremo y escasa visibilidad."
    },
    {
        "id": "R2",
        "conditions": {
            "difficulty": "Baja"
        },
        "conclusion": "Ideal para principiantes",
        "explanation": "Sendero accesible, bajo riesgo y menor exigencia física."
    },
    {
        "id": "R3",
        "conditions": {
            "location": "Parque Nacional",
            "motivation": "Naturaleza"
        },
        "conclusion": "Recomendado",
        "explanation": "Zonas del Parque Nacional permiten disfrutar del paisaje fueguino y observar fauna nativa."
    },
    {
        "id": "R4",
        "conditions": {
            "season": "Invierno"
        },
        "conclusion": "Precaución",
        "explanation": "En invierno, considerar luz solar limitada, frío extremo y terreno resbaladizo."
    },
    {
        "id": "P1",
        "conditions": {
        "location": "Río Grande",
        "season": "Verano"
        },
        "conclusion": "Recomendado: Pesca con mosca en Río Grande",
        "explanation": "Río Grande es reconocido mundialmente para pesca de trucha marrón en verano. Acceso con guía y permisos."
    },
    {
        "id": "P2",
        "conditions": {
        "location": "Tolhuin",
        "season": "Verano"
        },
        "conclusion": "Recomendado: Lago Yehuin",
        "explanation": "El Lago Yehuin ofrece aguas frías y buena pesca de trucha marrón durante el verano."
    },
    {
        "id": "P3",
        "conditions": {
        "location": "Tolhuin",
        "season": "Todo el año"
        },
        "conclusion": "Recomendado: Lago Fagnano",
        "explanation": "El Lago Fagnano permite pesca recreativa todo el año desde costa o embarcado. Acceso directo desde Tolhuin."
    },
    {
        "id": "P4",
        "conditions": {
        "motivation": "Pesca técnica"
        },
        "conclusion": "Sugerencia: Arroyo Claro",
        "explanation": "Pesca con mosca en Arroyo Claro, ideal para pescadores técnicos con caminata corta."
    },
    {
        "id": "P5",
        "conditions": {
        "location": "Ushuaia",
        "season": "Todo el año"
        },
        "conclusion": "Opcional: Lago Escondido",
        "explanation": "Lago Escondido es accesible todo el año desde la Ruta 3, con pesca recreativa habilitada."
    },
    {
        "id": "M1",
        "conditions": {
        "location": "Ushuaia",
        "motivation": "Cultura"
        },
        "conclusion": "Recomendado: Museo del Fin del Mundo",
        "explanation": "Este museo brinda una introducción completa a la historia, fauna y culturas fueguinas. Ideal para visitantes en Ushuaia con interés cultural."
    },
    {
        "id": "M2",
        "conditions": {
        "location": "Ushuaia",
        "motivation": "Cultura"
        },
        "conclusion": "Recomendado: Museo Marítimo y del Presidio",
        "explanation": "Ubicado en el ex presidio histórico, combina historia carcelaria, naval y arte contemporáneo. Muy valorado culturalmente."
    },
    {
        "id": "M3",
        "conditions": {
        "location": "Río Grande",
        "motivation": "Cultura"
        },
        "conclusion": "Recomendado: Museo Fueguino de Arte",
        "explanation": "Muestra obras locales y colecciones contemporáneas. Ideal para explorar el patrimonio artístico de la provincia."
    },
    {
        "id": "M4",
        "conditions": {
        "location": "Río Grande",
        "motivation": "Cultura"
        },
        "conclusion": "Recomendado: Museo Monseñor Fagnano",
        "explanation": "Museo de la Misión Salesiana con muestras sobre etnografía, historia rural e indígenas. Aporta valor cultural y educativo."
    },
    {
        "id": "M5",
        "conditions": {
        "location": "Ushuaia",
        "season": "Verano",
        "motivation": "Cultura"
        },
        "conclusion": "Recomendado: Casa Beban (eventos y exposiciones)",
        "explanation": "Espacio cultural activo en temporada estival con talleres, muestras temporales y arquitectura patrimonial fueguina."
    },
# Reglas relacionadas a deportes de invierno

    {
        "id": "D1",
        "conditions": {
        "location": "Ushuaia",
        "season": "Invierno",
        "motivation": "Ejercicio"
        },
        "conclusion": "Recomendado: Cerro Castor",
        "explanation": "El centro de esquí más austral del mundo. Cuenta con pistas para todos los niveles, alquiler de equipos y clases disponibles."
    },
    {
        "id": "D2",
        "conditions": {
        "location": "Ushuaia",
        "season": "Invierno",
        "motivation": "Naturaleza"
        },
        "conclusion": "Recomendado: Valle Tierra Mayor",
        "explanation": "Ideal para raquetas de nieve, trineos y caminatas en nieve. Ofrece experiencias guiadas en paisajes nevados fueguinos."
    },
    {
        "id": "D3",
        "conditions": {
        "location": "Ushuaia",
        "season": "Invierno",
        "motivation": "Paisaje"
        },
        "conclusion": "Recomendado: Glaciar Martial",
        "explanation": "Senderos señalizados con acceso a miradores panorámicos. Apto para caminatas sobre hielo y uso de raquetas."
    },
    {
        "id": "D4",
        "conditions": {
        "season": "Invierno",
        "motivation": "Aventura"
        },
        "conclusion": "Sugerido: Complejo Haruwen",
        "explanation": "Actividades como moto de nieve, trineo y esquí de travesía. Ideal para visitantes con espíritu aventurero en zonas más alejadas."
    },
    {
        "id": "D5",
        "conditions": {
        "location": "Ushuaia",
        "season": "Invierno",
        "motivation": "Cultura"
        },
        "conclusion": "Recomendado: Llanos del Castor",
        "explanation": "Propuesta cultural y recreativa con trineos, gastronomía regional y actividades para toda la familia."
    },
    {
        "id": "C5",
        "conditions": {
        "location": "Parque Nacional Tierra del Fuego",
        "motivation": "Cultura"
    },
        "conclusion": "Recomendado: Estafeta Postal del Fin del Mundo",
        "explanation": "Ubicada en Bahía Ensenada Zaratiegui, permite enviar postales con sello austral y forma parte del patrimonio cultural fueguino."
    },


]