def descending_order(num):
    lista_num = []
    for x in str(num):
        lista_num.append(int(x))
    for i in range(1, len(lista_num)):
        for j in range(0, (len(lista_num))-1):
            if lista_num[j+1] > lista_num[j]:
                aux = lista_num[j]
                lista_num[j] = lista_num[j+1]
                lista_num[j+1] = aux

    return int("".join(str(lista_num[i]) for i in range(0, len(lista_num))))


if __name__ == '__main__':
    print(descending_order(123456789))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
