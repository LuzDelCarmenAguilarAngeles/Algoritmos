def nba_extrap(ppg, mpg):
    # Si los minutos jugados son 0, retornamos 0
    if mpg == 0:
        return 0
    # Extrapolamos los puntos a 48 minutos
    extrapolated_ppg = (ppg / mpg) * 48
    # Redondeamos a la décima más cercana
    return round(extrapolated_ppg, 1)

# Solicitar al usuario que ingrese los puntos por partido y los minutos por partido
ppg = float(input("Ingresa los puntos por partido (ppg): "))
mpg = float(input("Ingresa los minutos por partido (mpg): "))

# Calcular los puntos extrapolados
extrapolated_points = nba_extrap(ppg, mpg)

# Mostrar el resultado
print(f"Puntos extrapolados para 48 minutos: {extrapolated_points}")
