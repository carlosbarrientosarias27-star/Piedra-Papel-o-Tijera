def mostrar_opciones():
    print("Elige una opción:")
    print("1 = Piedra")
    print("2 = Papel")
    print("3 = Tijera")


def obtener_eleccion_jugador():
    while True:
        try:
            opcion = int(input("Introduce el número de tu elección: "))
            if opcion in [1, 2, 3]:
                return opcion
            else:
                print("Opción no válida. Debe ser 1, 2 o 3.")
        except ValueError:
            print("Entrada inválida. Introduce un número.")


def convertir_eleccion(numero):
    opciones = {
        1: "Piedra",
        2: "Papel",
        3: "Tijera"
    }
    return opciones[numero]


# Programa principal
mostrar_opciones()
eleccion_numero = obtener_eleccion_jugador()
eleccion_nombre = convertir_eleccion(eleccion_numero)

print(f"Has elegido: {eleccion_nombre}") 

import random

def eleccion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

# Generar elección
computadora = eleccion_computadora()

# Mostrar elección por pantalla
print("La computadora eligió:", computadora) 