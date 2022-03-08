from copy import copy


def is_palindrom(frase_original: str):
    """ Funcion que verifica si una palabra es palindroma """

    if type(frase_original) != str:
        raise Exception("Valor ingresado incorrecto")
    else:
        frase = copy(frase_original)
        frase = frase.replace(" ", "")
        if len(frase) % 2 == 0:
            primer_mitad = frase[:len(frase)//2]
            segunda_mitad = frase[len(frase)//2:len(frase)]
        else:
            primer_mitad = frase[:len(frase) // 2]
            segunda_mitad = frase[(len(frase)//2)+1 : len(frase)+1]
        return True if primer_mitad == segunda_mitad[::-1] else False


if __name__ == '__main__':
    print("anita lava la tina" + ":", is_palindrom("anita lava la tina"))
    print("osso" + ":", is_palindrom("osso"))
    print("oso" + ":", is_palindrom("oso"))
    print("casa" + ":", is_palindrom("casa"))
