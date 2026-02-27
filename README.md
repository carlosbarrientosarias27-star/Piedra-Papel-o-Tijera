# Piedra-Papel-o-Tijera 

Un clásico juego de manos convertido en aplicación interactiva. Pon a prueba tu suerte y estrategia enfrentándote a la máquina en esta versión digital del juego más popular del mundo.

---

## 📋 Descripción del Proyecto

**Piedra, Papel o Tijera** es una aplicación de entretenimiento basada en el famoso juego de decisiones simultáneas. El jugador se enfrenta contra la computadora, que elige su opción de forma aleatoria. El objetivo es superar al rival seleccionando la opción ganadora según las reglas del juego.

Este proyecto está desarrollado con el propósito de practicar lógica de programación, manejo de eventos e interacción con el usuario.

---

## 🎮 ¿Cómo Jugar?

1. El jugador elige una de las tres opciones disponibles: **Piedra**, **Papel** o **Tijera**.
2. La computadora genera su elección de forma aleatoria.
3. Se comparan ambas elecciones y se determina un ganador según las reglas.
4. Se muestra el resultado de la ronda: **¡Ganaste!**, **Perdiste** o **Empate**.
5. El juego puede repetirse tantas veces como se desee.

---

## 📜 Reglas del Juego

| Tu elección | VS | Elección rival | Resultado     |
|:-----------:|:--:|:--------------:|:-------------:|
| 🪨 Piedra   | vs | ✂️ Tijera       | ✅ Ganas       |
| 📄 Papel    | vs | 🪨 Piedra       | ✅ Ganas       |
| ✂️ Tijera   | vs | 📄 Papel        | ✅ Ganas       |
| 🪨 Piedra   | vs | 📄 Papel        | ❌ Pierdes     |
| 📄 Papel    | vs | ✂️ Tijera       | ❌ Pierdes     |
| ✂️ Tijera   | vs | 🪨 Piedra       | ❌ Pierdes     |
| Cualquiera  | vs | Igual           | 🤝 Empate      |

### Resumen de victorias:
- 🪨 **Piedra** aplasta a ✂️ Tijera
- 📄 **Papel** envuelve a 🪨 Piedra
- ✂️ **Tijera** corta a 📄 Papel

---

## 🚀 Características

- Interfaz sencilla e intuitiva
- Oponente controlado por la computadora con selección aleatoria
- Registro de puntuación por sesión
- Resultados mostrados en tiempo real

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** JavaScript / Python *(adaptar según tu stack)*
- **Interfaz:** HTML + CSS / Consola
- **Lógica:** Condicionales y generación de números aleatorios

---

## 📁 Estructura del Proyecto

```
piedra-papel-tijera/
│
├── index.html        # Interfaz principal
├── style.css         # Estilos visuales
├── app.js            # Lógica del juego
└── README.md         # Documentación del proyecto
```

---

## 👤 Autor

Desarrollado con ❤️ como proyecto de práctica.

---

## 📄 Licencia

Este proyecto está bajo la licencia [MIT](https://opensource.org/licenses/MIT). Puedes usarlo, modificarlo y distribuirlo libremente.