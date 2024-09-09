import math
def dating_age_range(age):
    if age <= 14:
        min_age = math.floor(0.9 * age)
        max_age = math.floor(1.1 * age)
    else:
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)

    return f"{min_age}-{max_age}"

# Ingresar edad por consola
try:
    age = int(input("Ingresa tu edad: "))
    if 1 <= age <= 100:
        print(f"El rango de edad recomendado para ti es: {dating_age_range(age)}")
    else:
        print("Por favor ingresa una edad válida entre 1 y 100.")
except ValueError:
    print("Entrada inválida. Por favor ingresa un número entero.")
