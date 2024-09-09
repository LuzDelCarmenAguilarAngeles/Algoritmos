def total_pressure(M1, M2, m1, m2, V, T):
    # Constante de los gases (R)
    R = 0.082  # dm^3 * atm / K * mol

    # Convertir temperatura a Kelvin
    T_kelvin = T + 273.15

    # Calcular la presión total usando la fórmula
    P_total = ((m1 / M1) + (m2 / M2)) * R * T_kelvin / V

    return P_total
# Solicitar los valores de entrada al usuario
M1 = float(input("Ingresa la masa molar del gas 1 (g/mol): "))
M2 = float(input("Ingresa la masa molar del gas 2 (g/mol): "))
m1 = float(input("Ingresa la masa presente del gas 1 (g): "))
m2 = float(input("Ingresa la masa presente del gas 2 (g): "))
V = float(input("Ingresa el volumen del recipiente (dm^3): "))
T = float(input("Ingresa la temperatura (°C): "))

# Calcular la presión total
P_total = total_pressure(M1, M2, m1, m2, V, T)

# Mostrar el resultado
print(f"La presión total es: {P_total:.2f} atm")
