# 🪨📄✂️ Piedra, Papel o Tijera — Suite de Proyectos

Repositorio que agrupa dos proyectos relacionados con el clásico juego **Piedra, Papel o Tijera**, desarrollados en Python: una implementación completa con arquitectura modular y su correspondiente proyecto de prueba independiente.

---

# 📁 Estructura del Repositorio

```
├── Piedra_Papel_Tijera/
│   ├── docs/
│   │   ├── asistencia_ia.md
│   │   └── caso_edge.md
│   ├── src/
│   │   ├── __init__.py
│   │   ├── interfaz.py
│   │   ├── logica.py
│   │   └── utilidades.py
│   ├── test/
│   │   └── src/
│   │       ├── __init__.py
│   │       ├── test_interfaz.py
│   │       ├── test_logica.py
│   │       └── test_utilidades.py
│   ├── __init__.py
│   ├── test_main.py
│   ├── .gitignore
│   ├── LICENSE
│   ├── main.py
│   ├── README.md
│   └── requirements.txt
│
└── Proyecto de Prueba/
    ├── __init__.py
    ├── juego.py
    └── Readme.md
```

---

# 🎮 Proyecto 1 — Piedra_Papel_Tijera

Implementación principal del juego con una arquitectura modular bien definida, documentación técnica y suite de pruebas unitarias.

## ✨ Características

- Separación de responsabilidades en capas: lógica, interfaz y utilidades.
- Documentación de asistencia con IA y casos edge.
- Suite de tests unitarios para cada módulo.
- Código limpio, mantenible y extensible.

## 📦 Módulos (`src/`)

| Archivo | Descripción |
|---|---|
| `logica.py` | Reglas del juego: determina el ganador según la elección de cada jugador. |
| `interfaz.py` | Gestión de la interacción con el usuario (entrada/salida). |
| `utilidades.py` | Funciones auxiliares reutilizables (validaciones, formateo, etc.). |
| `main.py` | Punto de entrada principal de la aplicación. |

## 🧪 Tests (`test/src/`)

| Archivo | Descripción |
|---|---|
| `test_logica.py` | Pruebas unitarias de las reglas del juego. |
| `test_interfaz.py` | Pruebas de la capa de interfaz. |
| `test_utilidades.py` | Pruebas de las funciones auxiliares. |
| `test_main.py` | Pruebas de integración del flujo principal. |

## 📄 Documentación (`docs/`)

- **`asistencia_ia.md`** — Notas y apoyo generado con asistencia de inteligencia artificial.
- **`caso_edge.md`** — Documentación de casos borde identificados y su tratamiento.

## 🚀 Instalación y Ejecución

```
# Clonar el repositorio
git clone <url-del-repositorio>
cd Piedra_Papel_Tijera

# Ejecutar el juego
python main.py
```

## 🧪 Ejecutar Tests

```
# Desde la raíz del proyecto
python -m pytest test/src/

# O ejecutar un test específico
python -m pytest test/src/test_logica.py
```

---

# 🧩 Proyecto 2 — Proyecto de Prueba

Proyecto independiente y simplificado que sirve como entorno de prueba o prototipo rápido del juego.

## ✨ Características

- Implementación ligera y directa del juego en un único archivo.
- Ideal para experimentar con la lógica central sin dependencias adicionales.

## 📦 Archivos

| Archivo | Descripción |
|---|---|
| `juego.py` | Implementación autónoma del juego Piedra, Papel o Tijera. |
| `__init__.py` | Inicialización del módulo. |
| `Readme.md` | Documentación específica del proyecto de prueba. |

## 🚀 Ejecución

```
cd "Proyecto de Prueba"
python juego.py
```

---

# 🛠️ Tecnologías

- **Lenguaje:** Python 3.14


---

# 📜 Licencia

Este proyecto se distribuye bajo los términos indicados en el archivo [`LICENSE`](Piedra_Papel_Tijera/LICENSE MIT).

---