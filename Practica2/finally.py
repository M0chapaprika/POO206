
try:
    a = 10
    b = 2
    resultado = a / b
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
finally:
    print("Este mensaje se muestra siempre")