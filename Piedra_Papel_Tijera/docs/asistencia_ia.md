# Documentación de Asistencia IA - Proyecto Piedra, Papel, Tijera 

## 1. Registro de Prompts Utilizados
En esta sección se detallan las interacciones clave con la IA para el desarrollo de la lógica, la interfaz y las pruebas.

## Generación de Lógica Core (src/logica.py)

- Prompt: "Actúa como un desarrollador senior de Python. Crea una función que determine el ganador de Piedra, Papel o Tijera utilizando un diccionario para mapear las reglas y evitar múltiples sentencias 'if-else'. Debe manejar casos de empate y entradas inválidas."

- Resultado: Se implementó una lógica limpia basada en un esquema de "vence a", facilitando la escalabilidad (por ejemplo, para añadir Lagarto o Spock en el futuro).

## Estructura de Pruebas Unitarias (test/src/)

- Prompt: "Genera un script de pruebas usando unittest para validar la lógica del juego. Necesito casos de prueba para: victoria del usuario, victoria de la CPU, empate y manejo de strings en mayúsculas/minúsculas."

- Resultado: Creación de test_logica.py, asegurando un 100% de cobertura en la toma de decisiones del juego.

## Refactorización de Interfaz (src/interfaz.py)

- Prompt: "Tengo este código de consola. ¿Cómo puedo separar los 'print' y 'input' de la lógica de negocio para seguir el principio de responsabilidad única?"

# 2. Reflexión Final sobre el uso de IA
El uso de herramientas de IA generativa en este proyecto ha permitido acelerar el ciclo de desarrollo, especialmente en la maquetación de pruebas y la resolución de errores de importación (problemas comunes con los archivos __init__.py en Python).

## Puntos Positivos 

- Eficiencia en Boilerplate: La creación de la estructura de carpetas y archivos base fue casi instantánea.

- Calidad del Código: La IA sugirió el uso de diccionarios en lugar de condicionales anidados, lo que hace el código más legible y "Pythonic".

- Aprendizaje: Ayudó a comprender mejor la jerarquía de módulos dentro de la carpeta test/src/.

## Desafíos y Aprendizaje

- Contexto de Rutas: En varios momentos, la IA sugirió rutas de importación que no coincidían con la estructura real de mi proyecto. Fue necesario corregir manualmente los sys.path o las importaciones relativas para que main.py reconociera los módulos de src.

- Pensamiento Crítico: No se debe copiar y pegar ciegamente. Fue necesario ajustar los nombres de las funciones para que fueran consistentes con el español (idioma elegido para el proyecto).

- Conclusión: La IA no reemplaza al programador, sino que actúa como un "copiloto" que permite centrarse en la arquitectura del software mientras ella se encarga de las tareas más repetitivas.