from config.opciones import OPCIONES

def mostrar_menu():
    print("=" * 40)
    print("🎮  PIEDRA - PAPEL - TIJERA  🎮")
    print("=" * 40)

    # Mostrar opciones ordenadas
    for clave in sorted(OPCIONES.keys()):
        nombre, emoji = OPCIONES[clave]
        print(f"{clave} - {emoji} {nombre}")

    print("0 - Salir")
    print("=" * 40)


def obtener_opcion_valida():
    while True:
        try:
            opcion = input("👉 Elige una opción: ").strip()
        except KeyboardInterrupt:
            # Si el usuario presiona Ctrl+C, salir limpiamente
            return "0"

        if not opcion:
            print("⚠️ No puedes dejar el campo vacío.")
            continue

        if opcion in OPCIONES or opcion == "0":
            return opcion

        # Mensaje dinámico según opciones disponibles
        opciones_validas = ", ".join(sorted(OPCIONES.keys()))
        print(f"⚠️ Opción inválida. Debes elegir {opciones_validas} o 0.")