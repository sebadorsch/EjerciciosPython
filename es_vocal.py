def is_vocal(letra):
    """ Funcion que verifica si una letra pasada es vocal"""

    vocales = ["a", "e", "i", "o", "u"]

    if type(letra) != str:
        raise Exception("Error en el tipo de variable")
    else:
        return True if letra in vocales else False


if __name__ == '__main__':
    print(is_vocal("a"))
    print(is_vocal("e"))
    print(is_vocal("i"))
    print(is_vocal("o"))
    print(is_vocal("u"))
    print(is_vocal("b"))