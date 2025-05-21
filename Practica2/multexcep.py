
try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    
    resultado = num1 / num2
    
    print("El resultado de la división es: ", resultado)

except (ValueError, ZeroDivisionError) as e:
    print("Error: ", e)
    print("Por favor ingrese números válidos y asegúrese de no dividir por cero.")