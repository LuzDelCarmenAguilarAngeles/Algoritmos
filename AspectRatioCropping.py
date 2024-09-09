import math

def convert_to_16_9(x, y):
    # La altura (Y) se mantiene igual
    height = y
    # Calculamos la nueva anchura (X) para una relación de aspecto 16:9
    new_width = (16 / 9) * height
    # Redondeamos hacia arriba para obtener un número entero
    new_width_rounded = math.ceil(new_width)
    return new_width_rounded, height

# Leer valores desde la consola
x_res = int(input("Ingresa el ancho (X) de la resolución: "))
y_res = int(input("Ingresa la altura (Y) de la resolución: "))

# Convertir a la resolución de aspecto 16:9
new_x, new_y = convert_to_16_9(x_res, y_res)

# Mostrar el resultado
print(f"Resolución con aspecto 16:9 manteniendo la altura {y_res}: {new_x} × {new_y}")
