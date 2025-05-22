
edad = -5

try:
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    elif edad < 18:
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")
except ValueError:
    print("Error")