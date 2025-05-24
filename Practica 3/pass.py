for i in range(5):
    try:
        contraseña = str(input("Introduce una contraseña: "))

        if len(contraseña) < 10:
            raise ValueError("Contraseña demasiado corta")

        if not any(caracter.isdigit() for caracter in contraseña):
            raise ValueError("Debe contener al menos un número")

        if not any(not caracter.isalnum() for caracter in contraseña):
            raise ValueError("Debe contener al menos un carácter especial")

        print("Contraseña válida")

    except ValueError as e:
        print(f"Error: {e}")
