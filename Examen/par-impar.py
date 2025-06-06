
for i in range(1, 5):
    try:
        numero1=(int(input("Introduce un numero par entre 200 y 400: ")))
        
        if numero1 >= 200 and numero1 <=400:
            if numero1 % 2 == 0:
                for num in range(numero1, 401):
                    if num % 2 == 0:
                        print ("Resultado: ", num)
            else:
                print("es impar, ingresa un numero par", numero1)
        else:
            print("Debe de ser mayor a 200 y menor a 400")
    except ValueError:
        print("Error: ", ValueError)
        