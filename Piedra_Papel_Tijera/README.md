# ✊✋✌️ Piedra, Papel o Tijera

Un juego clásico de **Piedra, Papel o Tijera** implementado en Python, con interfaz de usuario, lógica de juego separada y suite de pruebas automatizadas.

---

# 📋 Descripción

Este proyecto implementa el juego **Piedra, Papel o Tijera** siguiendo principios de diseño limpio y separación de responsabilidades. El jugador se enfrenta a una IA que elige su jugada de forma aleatoria. El juego lleva el registro de puntuaciones y permite jugar múltiples rondas.

---

# 🗂️ Estructura del Proyecto

```
Piedra_Papel_Tijera/
├── docs/
│   └── asistencia.ia/
│       ├── Mejoras Aplicadas y Casos Edge.md
│       ├── Prompt.md
│       └── Reflexión Final.md
├── src/
│   ├── __init__.py
│   ├── interfaz.py       # Manejo de entrada/salida con el usuario
│   ├── logica.py         # Lógica central del juego
│   └── utilidades.py     # Funciones auxiliares
├── test/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── test_interfaz.py
│   │   ├── test_logica.py
│   │   └── test_utilidades.py
│   ├── __init__.py
│   └── test_main.py
├── __init__.py
├── .gitignore
├── LICENSE
├── main.py               # Punto de entrada principal
├── README.md
└── requirements.txt
```

---

# 🎮 Reglas del Juego

El juego sigue las reglas clásicas de **Piedra, Papel o Tijera**:

| Jugada del jugador | Jugada de la IA | Resultado     |
|--------------------|-----------------|---------------|
| ✊ Piedra          | ✌️ Tijera        | 🏆 Jugador gana |
| ✋ Papel           | ✊ Piedra        | 🏆 Jugador gana |
| ✌️ Tijera          | ✋ Papel         | 🏆 Jugador gana |
| ✊ Piedra          | ✋ Papel         | 💀 IA gana      |
| ✋ Papel           | ✌️ Tijera        | 💀 IA gana      |
| ✌️ Tijera          | ✊ Piedra        | 💀 IA gana      |
| Cualquiera         | La misma        | 🤝 Empate       |

## Resumen de combinaciones ganadoras

- **Piedra** aplasta a **Tijera**
- **Papel** envuelve a **Piedra**
- **Tijera** corta a **Papel**

---

# 🚀 Instalación y Uso

## Requisitos previos

- Python 3.14

## Instalación

```
# Clonar el repositorio
git clone https://github.com/tu-usuario/Piedra_Papel_Tijera.git
cd Piedra_Papel_Tijera
```

## Ejecutar el juego

```
python main.py
```

---

# 🧪 Ejecutar las pruebas

```
# Ejecutar todos los tests
python -m pytest test/

# Ejecutar un módulo específico
python -m pytest test/src/test_logica.py
```

---

## 🏗️ Arquitectura

El proyecto está dividido en tres módulos principales dentro de `src/`:

- **`logica.py`** — Contiene las reglas del juego: determina el ganador de cada ronda, genera la jugada aleatoria de la IA y gestiona el marcador.
- **`interfaz.py`** — Gestiona toda la interacción con el usuario: muestra mensajes, recibe la jugada elegida y presenta los resultados.
- **`utilidades.py`** — Funciones de apoyo reutilizables (validaciones, formateo de texto, etc.).

---

## 📄 Licencia

Este proyecto está bajo la licencia especificada en el archivo [LICENSE](LICENSE).