from config.opciones import OPCIONES

def mostrar_menu():
    print("=" * 40)
    print("🎮  PIEDRA - PAPEL - TIJERA  🎮")
    print("=" * 40)

    for clave, valor in OPCIONES.items():
        print(f"{clave} - {valor[1]} {valor[0]}")

    print("0 - Salir")
    print("=" * 40)

def obtener_opcion_valida():
    while True:
        opcion = input("👉 Elige una opción: ").strip()

        if opcion == "":
            print("⚠️ No puedes dejar el campo vacío.")
            continue

        if opcion.startswith("-"):
            print("⚠️ No se permiten números negativos.")
            continue

        if opcion in OPCIONES or opcion == "0":
            return opcion

        print("⚠️ Opción inválida. Debes elegir 1, 2, 3 o 0.")