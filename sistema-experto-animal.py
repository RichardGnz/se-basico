base_conocimientos = {
    "plumas": ["pajaro"],
    "vuela": ["pajaro", "mosca"],
    "pico": ["pajaro"],
    "pelaje": ["perro", "gato"],
    "ladra": ["perro"],
    "maulla": ["gato"],
    "escamas": ["pez"],
    "nada": ["pez"]
}

def motor_inferencia(caracteristicas):
    animales = set()
    for caracteristica in caracteristicas:
        if caracteristica in base_conocimientos:
            animales.update(base_conocimientos[caracteristica])
        else:
            print(f"Advertencia: La característica '{caracteristica}' no se reconoce y se ignorará.")
    return list(animales)

while True:
    print("Las características disponibles son: " + ", ".join(base_conocimientos.keys()))
    entrada = input("Por favor, ingresa las características del animal separadas por comas (o escribe 'finalizar' para terminar): ")
    if entrada.lower() == 'finalizar':
        break
    caracteristicas = entrada.split(",")
    try:
        resultado = motor_inferencia(caracteristicas)
        if resultado:
            print(resultado)
        else:
            print("No se encontraron animales que coincidan con las características dadas.")
    except Exception as e:
        print(f"Se produjo un error: {e}")
