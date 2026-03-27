def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    pass
    contraseña=input()
    largo=len(contraseña)
    if largo>=8 and (("1" in contraseña) ==True or ("2" in contraseña) ==True or ("3" in contraseña) ==True or ("4" in contraseña) ==True or ("5" in contraseña) ==True or ("6" in contraseña) ==True or ("7" in contraseña) ==True or ("8" in contraseña) ==True or ("9" in contraseña) ==True or ("0" in contraseña) ==True):
        print("Contraseña valida")
    elif largo<8 and (("1" in contraseña) ==True or ("2" in contraseña) ==True or ("3" in contraseña) ==True or ("4" in contraseña) ==True or ("5" in contraseña) ==True or ("6" in contraseña) ==True or ("7" in contraseña) ==True or ("8" in contraseña) ==True or ("9" in contraseña) ==True or ("0" in contraseña) ==True)== False:
        print ("Contraseña muy corta\nDebe contener un numero")
    elif largo<8:
        print ("Contraseña muy corta")
    elif (("1" in contraseña) ==True or ("2" in contraseña) ==True or ("3" in contraseña) ==True or ("4" in contraseña) ==True or ("5" in contraseña) ==True or ("6" in contraseña) ==True or ("7" in contraseña) ==True or ("8" in contraseña) ==True or ("9" in contraseña) ==True or ("0" in contraseña) ==True)== False:
        print ("Debe contener un numero")

