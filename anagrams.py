
def anagrams(word, words):
    respuesta = []
    for x in words:
        if "".join(sorted(word)) == "".join(sorted(x)):
            respuesta.append(x)
    return respuesta


if __name__ == '__main__':
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])