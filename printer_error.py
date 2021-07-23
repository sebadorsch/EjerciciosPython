import re

def printer_error(s):
    lista = (re.compile('[a-m]')).findall(s)
    errores = len(s)-len(lista)
    return "{}/{}".format(errores, len(s))


if __name__ == '__main__':
    print(printer_error("aajjfdjsdhppp"))