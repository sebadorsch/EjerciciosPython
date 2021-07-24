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


if __name__ == '__main__':
    print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]),
                       "apples, pears\ngrapes\nbananas")
    print(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
