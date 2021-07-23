"""def find_outlier(integers):
    pares = []
    impares = []
    for num in integers:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    if len(pares) == 1:
        return pares[0]
    else:
        return impares[0]
"""


def find_outlier(integers):
    impares = [x for x in integers if x%2 != 0]
    pares = [x for x in integers if x%2 == 0]
    return impares[0] if len(impares)<len(pares) else pares[0]


if __name__ == '__main__':
    print(find_outlier([2, 4, 6, 8, 10, 3]), 3)
    print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
    print(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)