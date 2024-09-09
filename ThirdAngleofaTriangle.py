def third_angle(angle1, angle2):
    # La suma de los ángulos en un triángulo es 180
    return 180 - (angle1 + angle2)

# Solicitar al usuario que ingrese los dos ángulos
angle1 = int(input("Ingresa el primer ángulo: "))
angle2 = int(input("Ingresa el segundo ángulo: "))

# Calcular el tercer ángulo
third = third_angle(angle1, angle2)

# Mostrar el resultado
print(f"El tercer ángulo es: {third} grados")
