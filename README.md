# 🎮 Piedra, Papel o Tijera

Un juego clásico de **Piedra, Papel o Tijera** para la terminal, desarrollado en Python. Juega contra la computadora, lleva el control de tus victorias y consulta tu resumen al finalizar cada partida.

---

## 📋 Descripción

Este proyecto implementa el juego Piedra, Papel o Tijera en modo consola. El jugador elige su opción a través de un menú interactivo, la computadora realiza su elección de forma aleatoria, y el programa determina el ganador de cada ronda. Al terminar la partida se muestra un resumen con estadísticas detalladas.

---

## 🗂️ Estructura del proyecto

```
PIEDRA-PAPEL-O-TIJERA/
├── .gitignore               # Archivos y carpetas ignorados por Git
├── LICENSE                  # Licencia del proyecto
├── main.py                  # Archivo principal que ejecuta el juego
├── README.md                # Documentación del proyecto
├── requirements.txt         # Dependencias del proyecto
│
├── config/                  # Configuración del juego
│   ├── __init__.py          # Hace que la carpeta sea un paquete
│   └── opciones.py          # Definición de las opciones (Piedra, Papel, etc.)
│
├── core/                    # Lógica central del negocio
│   ├── __init__.py          #
│   ├── juego.py             # Flujo principal de la partida
│   └── logica.py            # Reglas para determinar ganadores
│
├── ui/                      # Interfaz de Usuario (Consola)
│   ├── __init__.py          #
│   ├── menus.py             # Gestión de menús de selección
│   └── pantalla.py          # Visualización de textos y bienvenida
│
├── utils/                   # Herramientas auxiliares
│   ├── __init__.py          #
│   └── helpers.py           # Funciones de apoyo (ej: limpiar pantalla)
│
├── test/                    # Suite de Pruebas Unitarias
│   ├── __init__.py          #
│   ├── test_main.py         # Pruebas para el punto de entrada
│   ├── config/              # Tests de configuración
│   │   ├── __init__.py      #
│   │   └── test_opciones.py #
│   ├── core/                # Tests de la lógica central
│   │   ├── __init__.py      #
│   │   ├── test_juego.py    #
│   │   └── test_logica.py   #
│   ├── ui/                  # Tests de interfaz
│   │   ├── __init__.py      #
│   │   ├── test_menus.py    #
│   │   └── test_pantalla.py #
│   └── utils/               # Tests de utilidades
│       ├── __init__.py      #
│       └── test_helpers.py  #
│
├── docs/                    # Documentación adicional
└── .qodo/                   # Archivos de configuración de herramientas (AI/IDE)
```

---

## ⚙️ Requisitos

- Python 3.14
- No requiere dependencias externas (solo módulos de la librería estándar: `os`, `random`, `time`)

---

## 🚀 Cómo ejecutar

```bash
python juego.py
```

---

## 📜 Reglas del juego

| Elección | Vence a |
|----------|---------|
| 🪨 Piedra | ✂️ Tijera |
| 📄 Papel  | 🪨 Piedra |
| ✂️ Tijera | 📄 Papel  |

- Si ambos jugadores eligen lo mismo, la ronda es un **empate**.
- El jugador puede disputar tantas rondas como desee dentro de una partida.
- Al salir, se muestra un **resumen final** con victorias, derrotas, empates y porcentaje de victorias.
- Al terminar una partida, el jugador puede iniciar una nueva sin cerrar el programa.

---

## 🕹️ Cómo jugar

1. Al iniciar, se muestra la pantalla de bienvenida con las reglas.
2. En cada ronda, elige una opción del menú:
   - `1` → 🪨 Piedra
   - `2` → 📄 Papel
   - `3` → ✂️ Tijera
   - `0` → Salir y ver el resumen
3. La computadora elige aleatoriamente su opción.
4. Se muestra el resultado de la ronda.
5. Al finalizar la partida, se presenta el resumen estadístico.
6. Puedes elegir jugar otra partida o salir del programa.

---

## 📊 Resumen final

Al concluir cada partida se muestran:

- 🏆 Número de victorias
- 💻 Número de derrotas
- 🤝 Número de empates
- 📈 Porcentaje de victorias
- Resultado global: ganador, perdedor o empate general

---

## 🧩 Funciones principales

| Función | Descripción |
|---|---|
| `mostrar_bienvenida()` | Muestra la pantalla inicial con las reglas |
| `mostrar_menu()` | Despliega las opciones del juego |
| `obtener_opcion_valida()` | Valida la entrada del usuario |
| `obtener_eleccion_computadora()` | Genera la elección aleatoria de la computadora |
| `determinar_ganador()` | Evalúa quién ganó la ronda |
| `mostrar_resultado_ronda()` | Imprime el resultado de la ronda |
| `mostrar_resumen()` | Muestra las estadísticas finales |
| `jugar()` | Controla el flujo de una partida completa |
| `main()` | Punto de entrada; permite múltiples partidas |

---

## 👤 Autor

Desarrollado como proyecto de práctica en Python. 

--- 

## License 

Usa una Lincense MIT 