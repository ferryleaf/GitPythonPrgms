'''
Description - Transpose of a matrix is obtained by changing rows to columns
and columns to rows. In other words, transpose of A[ ][ ] is obtained by
changing A[ i ][ j ] to A[ j ][ i ].We are given a matrix of size m*n,
We have to print the transpose of the matrix.
'''


def mat_transpose(a):
    row = len(a)
    col = len(a[0])
    aT = [[(0) for _ in range(row)] for _ in range(col)]
    for i in range(row):
        for j in range(col):
            aT[j][i] = a[i][j]
    print(a)
    print(aT)


# Using List Comphrension Technique
def mat_transpose2(a):
    row = len(a)
    col = len(a[0])
    print(a)
    aT = [[a[j][i] for j in range(row)] for i in range(col)]
    print(aT)


if __name__ == '__main__':
    # Program to multiply two matrices using nested loops
    # 3x3 matrix
    a = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
    mat_transpose(a)

    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat_transpose(a)

    # 3x4 matrix
    b = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]
    mat_transpose(b)

    # 3x4 matrix
    b = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]
    mat_transpose2(b)
