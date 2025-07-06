def generar_prompt(entrada_sensor):
    prompt = (
        f"Estado del equipo {entrada_sensor['equipo_id']} registrado en {entrada_sensor['timestamp']}:\n"
        f"- Temperatura de aceite: {entrada_sensor['temperatura_aceite']} °C\n"
        f"- Nivel de fluidos: {entrada_sensor['nivel_fluidos']} %\n"
        f"- Voltaje de batería: {entrada_sensor['voltaje_bateria']} V\n"
        f"- Vibración: {entrada_sensor['vibracion']} mm/s\n\n"
        "Proponer acciones de mantenimiento si corresponde."
    )
    return prompt
