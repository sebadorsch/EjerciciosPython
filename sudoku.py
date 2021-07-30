def valid_solution(board):
    for fila in board:
        for j in fila:
            if fila.count(j) == 2:
                return False
    """for i in range(len(board)):
        aux = board[i]
        for j in range(9):
            if aux == board[j][i]:
                return False"""

    # Para terminar:

    for i in range(3):
        for j in range(3):
            aux = board[i][j]
            cont = 0
            for k in range(3):
                for l in range(3):
                    if aux == board[k][l]:
                        cont += 1
                if cont == 2:
                    return False
    return True


if __name__ == '__main__':

    print((valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                           [6, 7, 2, 1, 9, 5, 3, 4, 8],
                           [1, 9, 8, 3, 4, 2, 5, 6, 7],
                           [8, 5, 9, 7, 6, 1, 4, 2, 3],
                           [4, 2, 6, 8, 5, 3, 7, 9, 1],
                           [7, 1, 3, 9, 2, 4, 8, 5, 6],
                           [9, 6, 1, 5, 3, 7, 2, 8, 4],
                           [2, 8, 7, 4, 1, 9, 6, 3, 5],
                           [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True))
"""
    print((valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                           [6, 7, 2, 1, 9, 0, 3, 4, 9],
                           [1, 0, 0, 3, 4, 2, 5, 6, 0],
                           [8, 5, 9, 7, 6, 1, 0, 2, 0],
                           [4, 2, 6, 8, 5, 3, 7, 9, 1],
                           [7, 1, 3, 9, 2, 4, 8, 5, 6],
                           [9, 0, 1, 5, 3, 7, 2, 1, 4],
                           [2, 8, 7, 4, 1, 9, 6, 3, 5],
                           [3, 0, 0, 4, 8, 1, 1, 7, 9]]), False))"""