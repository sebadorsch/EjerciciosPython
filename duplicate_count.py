def duplicate_count(text):
    """letras = []
    contador = 0
    for i in range(len(text)-1):
        for j in range(i+1, len(text)):
            if text[i].lower() == text[j].lower() and text[j].lower() not in letras:
                letras.append(text[j].lower())
                contador += 1
    return contador
    """

    contador = 0
    for caracter in set(text.lower()):
        if text.lower().count(caracter) > 1:
            contador += 1
    return contador


"""
def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])
"""

if __name__ == '__main__':
    print(duplicate_count("abcdeaB"), 2)

    print(duplicate_count("CyydJKcenFeY0hglG3GDQpzBjcEE1ZJ5gtBWhN7Yd44"), 11)
    print(duplicate_count("abcde"), 0)
    print(duplicate_count("abcdeaa"), 1)
    
    print(duplicate_count("Indivisibilities"), 2)