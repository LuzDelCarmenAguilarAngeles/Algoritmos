def usd_to_cny(usd):
    # Tasa de conversión de USD a CNY
    conversion_rate = 6.75
    # Convertir USD a CNY y formatear con dos decimales
    cny = usd * conversion_rate
    return f"{cny:.2f} Chinese Yuan"

def cny_to_usd(cny):
    # Tasa de conversión de CNY a USD
    conversion_rate = 1 / 6.75
    # Convertir CNY a USD y formatear con dos decimales
    usd = cny * conversion_rate
    return f"{usd:.2f} US Dollars"

# Menú para elegir la conversión
print("Selecciona la conversión que deseas realizar:")
print("1: Convertir de USD a CNY")
print("2: Convertir de CNY a USD")

# Obtener la opción del usuario
opcion = int(input("Ingresa el número de la opción deseada: "))

# Ejecutar la conversión según la opción seleccionada
if opcion == 1:
    usd = float(input("Ingresa la cantidad de dólares (USD): "))
    print(usd_to_cny(usd))
elif opcion == 2:
    cny = float(input("Ingresa la cantidad de yuanes (CNY): "))
    print(cny_to_usd(cny))
else:
    print("Opción no válida. Por favor, selecciona una opción del 1 o 2.")

