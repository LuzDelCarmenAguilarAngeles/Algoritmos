def mango(quantity, price):
    # Cada 3 mangos, 2 se pagan y 1 es gratis
    # El costo es el precio por el número de mangos pagados
    total_cost = (quantity - quantity // 3) * price
    return total_cost

# Solicitar al usuario que ingrese la cantidad de mangos y el precio por mango
quantity = int(input("Ingresa la cantidad de mangos: "))
price = float(input("Ingresa el precio por mango: "))

# Calcular el costo total
total = mango(quantity, price)

# Mostrar el resultado
print(f"El costo total de los mangos es: ${total}")
