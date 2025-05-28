
for i in range(0, 5):
    try:
        num = int(input("Ingresa un número entero positivo: "))
        if num > 0:
            for n in range(num, -1, -1):
                if n != 0:
                    print(n)
        else:
            print("El número debe ser mayor que cero >:(")
    except ValueError:
        print("Error: Ingresaste algo que no es un número")
