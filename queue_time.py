def queue_time(customers, n):
    filas = []
    if n > 1 and (len(customers) >= n):
        # Cargo la lista filas con los primeros valores de los customers
        for i in range(n):
            filas.append(customers[i])
        # Recorro lo que queda de customers
        for i in range(n, len(customers)):
            indice = 0
            # Se lo cargo al valor de filas mas chico
            for j in (range(n-1)):
                for k in range(j+1, n):
                    if filas[j] <= filas[k] and filas[k] <= filas[indice]:
                        indice = j
                    if j == range(n-1) and k == range(n):
                        indice = j
                        break
            filas[indice] += customers[i]
        return max(filas)
    elif len(customers)<n and len(customers)>0:
        # Cargo la lista filas con los primeros valores de los customers
        for i in range(len(customers)):
            filas.append(customers[i])
        return max(filas)
    else:
        sum = 0
        for i in customers:
            sum += i
        return sum


if __name__ == '__main__':
    """
    print(queue_time([], 1), 0)
    print(queue_time([5], 1), 5)
    print(queue_time([2], 5), 2)
    print(queue_time([1, 2, 3, 4, 5], 1), 15)
    print(queue_time([1, 2, 3, 4, 5], 100), 5)
    print(queue_time([2,2,3,3,4,4], 2), 9)
    
    """
    print(queue_time([8, 39, 6, 3, 6, 41, 20, 12, 26, 23, 47, 10, 39, 40, 27, 22], n=6), 72)