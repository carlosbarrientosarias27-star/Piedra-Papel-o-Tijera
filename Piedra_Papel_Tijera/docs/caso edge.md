# 🧪 Casos de Prueba (Edge Cases)

| Caso de Prueba | Entrada de Ejemplo | Comportamiento Esperado | Estado |
| :--- | :--- | :--- | :---: |
| **Entrada Vacía** | `""` | Lanzar `ValueError` o devolver un mensaje de error solicitando datos. | ⏳ Pendiente |
| **Letras / Texto Inválido** | `"hola"`, `"x"` | No debe romper el programa (evitar crash); debe solicitar la entrada de nuevo. | ⏳ Pendiente |
| **Números Negativos** | `-1` | El valor debe ser ignorado o marcado como inválido por el validador. | ⏳ Pendiente |
| **Fuera de Rango** | `99` | Si solo existen 3 opciones (1, 2, 3), cualquier otro número debe ser rechazado. | ⏳ Pendiente |