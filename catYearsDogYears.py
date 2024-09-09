#Programa que calcula la edad de perro y gato en humano...

def calculate_pet_ages(humanYears):

    # Inicializamos las variables para los años de gato y perro
    catYears = 0
    dogYears = 0

    # Calculamos los años de gato y perro basándonos en los años humanos
    if humanYears == 1:  # Al primer año
        catYears = 15
        dogYears = 15
    elif humanYears == 2:  # Al segundo año
        catYears = 15 + 9
        dogYears = 15 + 9
    else:  # A partir de 3 años
        catYears = 15 + 9 + (humanYears - 2) * 4
        dogYears = 15 + 9 + (humanYears - 2) * 5

    # Devuelve una lista con los años humanos, gato y perro
    return [humanYears, catYears, dogYears]

# Solicita la edad humana por consola
try:
    human_years_input = int(input("Introduce la edad en años humanos: "))
    # Llama a la función para los cálculos
    result = calculate_pet_ages(human_years_input)
    print(f"Los años humanos son: {result[0]}")#indica que se está utilizando un f-string (formatted string literal)
    print(f"Los años humanos de gato son: {result[1]}")
    print(f"Los años humanos de perro son: {result[2]}")
    # Imprime el tipo de datos devuelto por la función
    print(f"Tipo de datos devuelto: {type(result)}")

except ValueError:
    print("Por favor, introduce un número entero válido.")

