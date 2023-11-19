def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    sum_tl_to_br = 0
    sum_bl_to_tr = 0

    # add top left to bottom right adding all matrix[i][j]
    # [0][0], [1][1], [2][2], [3][3], [4][4] ...
    for i in range(0, len(matrix[0])):
        sum_tl_to_br += matrix[i][i]

    # add top right to bottom left adding all matrix[i][j]
    # where i starts at 0 and j starts at len(matrix[0])
    # [0][4], [1][3], [2][2], [3][1], [4][0] ...
    j = len(matrix[0])-1
    for i in range(0, len(matrix[0])):
        sum_bl_to_tr +=  matrix[i][j]
        j -= 1
    
    return sum_tl_to_br + sum_bl_to_tr