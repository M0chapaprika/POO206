
for i in range(0, 5):
    try:
        frase = input("Ingresa una frase: ")
        letra = input("Ingresa una letra: ")

        if len(letra) != 1:
            print("Debes ingresar solo una letra >:(")
        else:
            contador = 0
            for caracter in frase:
                if caracter == letra:
                    contador += 1
            print("La letra '" + letra + "' aparece " + str(contador) + " veces en la frase.")
            break   
    except ValueError:
        print("Error: Ocurrió un error inesperado")
