def digital_root(n):
    suma = 0
    for i in str(n):
        suma += int(i)
    if suma > 9:
        return digital_root(suma)
    else:
        return suma


if __name__ == '__main__':
    print(digital_root(16), 7)
    print(digital_root(942), 6)
    print(digital_root(132189), 6)
    print(digital_root(493193), 2)