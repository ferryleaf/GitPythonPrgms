'''
Given a Square Matrix of dimension N * N.
The task is to rotate the matrix in anti-clock wise direction by 90 degrees.


Example:
 1 2 3 4
 5 6 7 8
 9 10 11 12
 13 14 15 16

 4 8 12 16
 3 7 11 15
 2 6 10 14
 1 5 9 13


1 2 3 4
5 6 7 8
9 10 11 12

 4 8 12
 3 7 11
 2 6 10
 1 5 9

'''


def matrix_rotation(a):
    row = len(a)
    col = len(a[0])
    a_rot = [[(0) for _ in range(row)] for _ in range(col)]
    print(a)
    for i in range(col-1, -1, -1):
        for j in range(row):
            a_rot[(col-1)-i][j] = a[j][i]
    print(a_rot)
    print()


# Using List Comphresion
# [[(0)  column range]  row range]
# [[(0)  inner loop ]  outer loop]
def matrix_rotation2(a):
    row = len(a)
    col = len(a[0])
    print(a)
    a_rot = [[a[j][i] for j in range(row)] for i in range(col-1, -1, -1)]
    print(a_rot)
    print()


if __name__ == '__main__':
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    # Expected Output: 3X3
    # [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]
    matrix_rotation(a)

    # Expected Output: 3X4
    # [[4, 8, 12], [3, 7, 11], [2, 6, 10], [1, 5, 9]]
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matrix_rotation(a)

    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    matrix_rotation2(a)

    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matrix_rotation2(a)
