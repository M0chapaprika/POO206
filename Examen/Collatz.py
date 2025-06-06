
for i in range(1,5):
    
    try:
        numero1=(int(input("Ingresa un numero mayor a 1: ")))
        
        if numero1 >= 1:
            for num in range(numero1, -10, -1):
                if numero1 % 2 == 0:
                    numero1 = numero1 / 2
                    print(numero1)
                    
                    if numero1 == 1:
                        break
                else:
                    numero1 = (numero1 * 3) + 1
                    print(numero1)
                    
                    if numero1 == 1:
                        break
        else:
            print("Debes ingresar un numero mayor a 1")
    except ValueError:
        print("Error: ", ValueError)