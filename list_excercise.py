def solution(args):
    resultado = []
    i = 0
    while args[i]:
        acum, j = 0, 1
        while args[i] + j == args[i+j]:
            j += 1
        if j >= 3:
            resultado.append("".join('{}-{}'.format(args[i], args[i+j])))
        else:
            resultado.append(args[i])
        i += 1
    return resultado

if __name__ == '__main__':

    print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]),
                       '-6,-3-1,3-5,7-11,14,15,17-20')
    print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]), '-3--1,2,10,15,16,18-20')