def array_diff(mylist, pattern):
    pattern = set(pattern)
    lista_resultado = []
    for x in mylist:
        if x not in pattern:
            lista_resultado.append(x)
    return lista_resultado

"""
    pattern = set(pattern)
    return [x for x in mylist if x not in pattern]
"""


if __name__ == '__main__':
    print(array_diff([1, 2], [1]), [2], "a was [1,2], b was [1], expected [2]")
    print(array_diff([1, 2, 2], [1]), [2, 2], "a was [1,2,2], b was [1], expected [2,2]")
    print(array_diff([1, 2, 2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
    print(array_diff([1, 2, 2], []), [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
    print(array_diff([], [1, 2]), [], "a was [], b was [1,2], expected []")
    print(array_diff([1, 2, 3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")