'''
Matrices Multiplication
The multiplication of two matrices Am*n and Bn*p gives a matrix Cm*p.
It means number of columns in A must be equal to number of rows in B to
calculate C=A*B. To calculate element c11, multiply elements of 1st row of A
with 1st column of B and add them (5*1+6*4) which can be shown as:
'''


def mat_mul(a, b):
    # r: i X k  +  k X j
    # a: 3 X 3  b: 3 X 4
    '''
    Idea is simple
    Result matrix dims: a's [row] * b's [column] = [row][column]
    Remember Matrix multiplication strategy
    res[i][j]
    a[i][k] ---> i: 0 to row & k: 0 to row
    b[k][j] ---> k: 0 to row & j: 0 to col
    i: 0 to row & j: 0 to col & k: 0 to row
    '''
    row = len(a)
    col = len(b[1])
    res = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            for k in range(row):
                res[i][j] += a[i][k] * b[k][j]
    print(res)


if __name__ == '__main__':
    # Program to multiply two matrices using nested loops
    # 3x3 matrix
    a = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]

    # 3x4 matrix
    b = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]

    # result is 3x4
    # result = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
    # [[114, 160, 60, 27], [74, 97, 73, 14], [119, 157, 112, 23]]
    '''
    [114, 160, 60, 27]
    [74, 97, 73, 14]
    [119, 157, 112, 23]
    [[64, 44, 31, 0], [32, 36, 43, 0], [44, 48, 55, 0]]
    '''
    mat_mul(a, b)
