#Calcula la edad del perro y el gato en años humanos
def calculate_pet_ages(human_years):

    # Calcular años de gato
    #Al primer año
    if human_years == 1:
        cat_years = 15
        #Segundo año
    elif human_years == 2:
        #Tres años y mas
        cat_years = 15 + 9
    else:
        #Da una lista con los años humanos
        cat_years = 15 + 9 + (human_years - 2) * 4

    # Calcular años de perro
    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15 + 9
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]

# Ejemplo de uso
#human_years = 12  # puedes cambiar este valor a cualquier número entero positivo
#result = calculate_pet_ages(human_years) # Llama a la funcion para los calculos
#print(result)
#Esto imprimirá el resultado
# Pedir al usuario que ingrese los años humanos

#Se ingresan datos por consola
# Solicita al usuario que ingrese la cantidad de años humanos y la convierte en un número entero
human_years = int(input("Ingresa la cantidad de años humanos: "))

# Llama a la función 'calculate_pet_ages' pasando el número de años humanos como argumento
# Se espera que esta función devuelva una tupla con tres valores:
result = calculate_pet_ages(human_years)

# Imprime la edad en años humanos que fue ingresada por el usuario
print(f"Edad en años humanos: {result[0]}")

# Imprime la edad en años de gato, que es el segundo valor en la tupla 'result'
print(f"Edad en años de gato: {result[1]}")

# Imprime la edad en años de perro, que es el tercer valor en la tupla 'result'
print(f"Edad en años de perro: {result[2]}")