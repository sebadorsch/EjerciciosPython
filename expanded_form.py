def expanded_form(num):
    numstr = str(num)
    numeros = []
    for i in range(len(numstr)):
        if int(numstr[i]) > 0:
            numeros.append(numstr[i] + "0" * (len(numstr)-1 - i))
    if len(numeros) > 0:
        resultado = numeros[0]
    for x in range(1, len(numeros)):
        resultado = resultado + (" + " + numeros[x])
    return resultado


def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')


if __name__ == '__main__':
    print(expanded_form(12), '10 + 2')
    print(expanded_form(42), '40 + 2')
    print(expanded_form(70304), '70000 + 300 + 4')