
for i in range (0,5):
    try:
        num1=int(input("Ingresa un numero: "))
    
        if num1 % 2 == 0 and num1 > 0:
            print("El numero es par: ", num1)
        elif num1 % 2 == 1 and num1 > 0: 
            print("El numero es impar: ", num1)
        else:
            print("El numero no puede ser negativo >:(")
        break
    
    except ValueError:
        print("Error: Se ingreso algo que no es un numero entero.")   
        