# 🎮 Piedra, Papel o Tijera — Repositorio Unificado

Este repositorio contiene dos proyectos relacionados con el juego **Piedra, Papel o Tijera**: una implementación completa con arquitectura modular (`Piedra_Papel_Tijera`) y un proyecto de prueba de concepto (`Proyecto de Prueba`).

---

## 📁 Estructura del Repositorio

```
.
├── Piedra_Papel_Tijera/        # Proyecto principal
│   ├── docs/
│   │   ├── asistencia_ia.md
│   │   └── caso edge.md
│   ├── src/
│   │   ├── __init__.py
│   │   ├── interfaz.py
│   │   ├── logica.py
│   │   └── utilidades.py
│   ├── test/
│   │   ├── src/
│   │   │   ├── __init__.py
│   │   │   ├── test_interfaz.py
│   │   │   ├── test_logica.py
│   │   │   └── test_utilidades.py
│   │   ├── __init__.py
│   │   └── test_main.py
│   ├── __init__.py
│   ├── .gitignore
│   ├── LICENSE
│   ├── main.py
│   ├── README.md
│   └── requirements.txt
│
└── Proyecto de Prueba/         # Proyecto de prueba de concepto
    ├── __init__.py
    ├── juego.py
    └── Readme.md
```

---

## 🪨📄✂️ Proyecto Principal — `Piedra_Papel_Tijera`

Implementación completa del juego Piedra, Papel o Tijera con separación de responsabilidades, cobertura de tests y documentación técnica.

### Descripción

El proyecto sigue una arquitectura modular dividida en tres capas principales:

| Módulo | Archivo | Responsabilidad |
|---|---|---|
| Lógica | `src/logica.py` | Reglas del juego, determinación del ganador |
| Interfaz | `src/interfaz.py` | Interacción con el usuario (entrada/salida) |
| Utilidades | `src/utilidades.py` | Funciones auxiliares y helpers |
| Principal | `main.py` | Punto de entrada de la aplicación |

### Requisitos

```bash
pip install -r requirements.txt
```

### Ejecución

```bash
python main.py
```

### Tests

El proyecto incluye tests unitarios para cada módulo:

```bash
# Ejecutar todos los tests
python -m pytest test/

# Ejecutar tests de un módulo específico
python -m pytest test/src/test_logica.py
python -m pytest test/src/test_interfaz.py
python -m pytest test/src/test_utilidades.py
```

### Documentación

- [`docs/asistencia_ia.md`](Piedra_Papel_Tijera/docs/asistencia_ia.md) — Descripción del uso de IA durante el desarrollo.
- [`docs/caso edge.md`](Piedra_Papel_Tijera/docs/caso%20edge.md) — Casos límite identificados y cómo se manejan.

---

## 🧪 Proyecto de Prueba — `Proyecto de Prueba`

Prototipo inicial o prueba de concepto del juego, con una implementación simplificada en un único archivo.

### Descripción

Versión reducida del juego contenida en `juego.py`, orientada a explorar la lógica básica antes de la implementación modular del proyecto principal.

### Ejecución

```bash
cd "Proyecto de Prueba"
python juego.py
```

---

## ⚖️ Licencia

Este proyecto se distribuye bajo los términos de la licencia incluida en el archivo [`LICENSE`](Piedra_Papel_Tijera/LICENSE).

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un *issue* o un *pull request* describiendo los cambios propuestos.
