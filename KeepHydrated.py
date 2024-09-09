import math

def litres(time):
    # Nathan bebe 0.5 litros por hora, y se redondea hacia abajo con math.floor
    return math.floor(time * 0.5)

# Solicitar al usuario que ingrese el tiempo en horas
time = float(input("Ingresa el tiempo de ciclismo en horas: "))

# Calcular la cantidad de litros que beberá Nathan
litros = litres(time)

# Mostrar el resultado
print(f"Nathan beberá {litros} litros de agua.")
