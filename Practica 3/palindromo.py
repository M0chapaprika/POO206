
for i in range(0,5):  
    try:
        texto = str(input("Introduce una cadena de texto: "))

        if not texto.replace(" ", "").isalpha():
            raise ValueError

        palabra = texto.lower().replace(" ", "")

        if palabra == palabra[::-1]:
            print("La cadena es un palíndromo.")
        else:
            print("La cadena no es un palíndromo.")

    except ValueError:
        print("Error: Ingresaste algo que no es una letra")
