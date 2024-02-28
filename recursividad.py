def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

if __name__ == "__main__":
    try:
        num = int(input("¿De qué número quieres saber el factorial? "))
        if num < 0:
            print("El número debe ser mayor o igual a 0.")
        else:
            print(f"El factorial de {num} es {factorial(num)}.")
    except:
        print("Se espera un número válido.")
