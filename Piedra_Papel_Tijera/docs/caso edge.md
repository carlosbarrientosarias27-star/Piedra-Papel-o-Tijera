# 1. Casos de Prueba (Edge Cases)
Basándome en tu solicitud, estos son los escenarios que debemos validar: 

Caso de Prueba,Entrada de Ejemplo,Comportamiento Esperado
Entrada Vacía,"""""",El sistema debe lanzar un ValueError o mostrar un mensaje de error solicitando datos.
Letras / Texto Inválido,"""hola"", ""x""",No debe romper el programa (evitar crash); debe solicitar la entrada de nuevo.
Números Negativos,-1,"Si se usa un menú numérico, el valor debe ser ignorado o marcado como inválido."
Fuera de Rango,99,"Si solo existen 3 opciones (1, 2, 3), cualquier otro número debe ser rechazado."