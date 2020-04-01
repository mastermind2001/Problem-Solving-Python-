# Determinant of n*n matrix

def base_case(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])


def sub_matrix(mat, j):
    matrix = []
    lst = ()
    for n in range(len(mat)):
        lst = ()
        for m in range(len(mat)):
            if n != 0 and m != j:
                lst += mat[n][m],
        if len(lst) > 0:
            matrix.append(list(lst))
    return matrix


def is_valid_matrix(matrix):
    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            return False
    return True


def determinant(mat):
    if not is_valid_matrix(mat):
        return 'Not a square matrix'

    if len(mat) <= 2:
        return base_case(mat)
    
    i = 0
    summ = 0

    for j in range(len(mat)):
        summ += ((-1)**(i+j+2)) * mat[i][j] * determinant(sub_matrix(mat, j))

    return summ


# sample input 4*4 matrix
print(determinant([
    [1, 8, 5, 7], [9, 4, 7, 6], [8, 2, 1, 4], [5, 8, 4, 9]
]))
