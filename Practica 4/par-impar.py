
for i in range(0,5):
    try: 
        num=int(input("Ingresa un numero positivo: "))
        if(num >10):
                for n in range(3, num + 1):
                    if(n % 2 != 0):
                        print(n)
        elif(num > 0):
            print("No se aceptan numeros menores a 10")   
        else:
            print("No se aceptan numeros negativos >:(")    

    except ValueError:
        print("Error: Ingresaste algo que no es un numero")
