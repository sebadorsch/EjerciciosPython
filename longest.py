"""
import string

def longest(a, b):
    if len(a) < len(b):
        longitud = len(b)
    else:
        longitud = len(a)
    letras = list(string.ascii_lowercase)
    nueva_palabra = ""
    for letra in letras:
        if letra in a:
            nueva_palabra += letra
            if len(nueva_palabra) == longitud: break
        elif letra in b:
            nueva_palabra += letra
            if len(nueva_palabra) == longitud: break
    return nueva_palabra
"""


def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


if __name__ == '__main__':
    a = "xyaabbbccccdefww"
    b = "xxxxyyyyabklmopq"
    print(longest(a, b))  # -> "abcdefklmopqwxy"
