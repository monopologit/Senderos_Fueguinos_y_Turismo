# sistema_experto/engine/inference.py

def match_condition(user_value, rule_value):
    """Evalúa si la condición del usuario satisface la condición de la regla"""
    if isinstance(rule_value, str):
        return user_value == rule_value
    if isinstance(rule_value, (int, float)):
        return user_value == rule_value
    if isinstance(rule_value, dict):
        # Comparador numérico (por ejemplo, {">": 4})
        for op, val in rule_value.items():
            if op == "<" and not user_value < val:
                return False
            if op == "<=" and not user_value <= val:
                return False
            if op == ">" and not user_value > val:
                return False
            if op == ">=" and not user_value >= val:
                return False
            if op == "!=" and not user_value != val:
                return False
            if op == "==" and not user_value == val:
                return False
        return True
    return False  # Por defecto

def infer_conclusion(rules, user_facts):
    """Busca las reglas que coinciden con los hechos del usuario y devuelve las conclusiones aplicables"""
    matched_rules = []

    for rule in rules:
        conditions_met = True
        for key, expected_value in rule["conditions"].items():
            actual_value = user_facts.get(key)

            if actual_value is None or not match_condition(actual_value, expected_value):
                conditions_met = False
                break  # Una condición no se cumple → no aplicamos regla

        if conditions_met:
            matched_rules.append({
                "rule_id": rule["id"],
                "conclusion": rule["conclusion"],
                "explanation": rule["explanation"]
            })

    return matched_rules
