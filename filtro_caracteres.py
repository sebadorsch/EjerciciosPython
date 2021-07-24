def solution(string, markers):
    renglones = string.split("\n")
    respuesta = ""
    for renglon in renglones:
        for caracter in markers:
            if caracter in renglon:
                if renglon[renglon.find(caracter) - 1] == " ":
                    renglon = renglon[:renglon.find(caracter)-1]
                else:
                    renglon = renglon[:renglon.find(caracter)]
        respuesta = respuesta + (renglon+'\n')

    return respuesta[:-1]


def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)


if __name__ == '__main__':
    print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]),
                       "apples, pears\ngrapes\nbananas")
    print(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
