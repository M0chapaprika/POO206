for i in range(0, 5):
    try:
        año = int(input("Ingresa un año: "))
        
        if año > 0:
            if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
                print("El año es bisiesto:", año)
            else:
                print("El año no es bisiesto:", año)
        else:
            print("No se aceptan valores negativos >:(")
        break
    except ValueError:
        print("Error: Se ingresó algo que no es un número entero.")