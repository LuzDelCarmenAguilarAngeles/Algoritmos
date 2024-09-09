def round_to_two_decimal_places(number):
    return round(number, 2)


def main():
    while True:
        try:
            # Pedir al usuario que ingrese un número
            user_input = input("Ingresa un número para redondear (o 'salir' para terminar): ")

            if user_input.lower() == 'salir':
                print("Programa terminado.")
                break

            # Convertir la entrada del usuario a un número flotante
            number = float(user_input)

            # Redondear el número y mostrar el resultado
            rounded_num = round_to_two_decimal_places(number)
            print(f'Original: {number:.2f}, Redondeado: {rounded_num:.2f}')

        except ValueError:
            print("Entrada inválida. Por favor ingresa un número válido o 'salir' para terminar.")


if __name__ == "__main__":
    main()
