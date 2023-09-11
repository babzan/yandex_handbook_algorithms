def matrix_sum(matrix_A, matrix_B):
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix_A[i][j] + matrix_B[i][j])
        result.append(row)

    return result


def fillMatrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append([int(x) for x in input().split()])

    return matrix


def printResult(matrix, rows):
    for i in range(rows):
        print(*matrix[i])


size = [int(x) for x in input().split()]
rows = size[0]
cols = size[1]

matrix_A = fillMatrix(rows)
matrix_B = fillMatrix(rows)

printResult(matrix_sum(matrix_A, matrix_B), rows)
