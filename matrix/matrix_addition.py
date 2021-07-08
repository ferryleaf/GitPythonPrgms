'''
Add 2 matrix
'''


def mat_add(a, b):
    m = len(a)
    n = len(b[0])
    # c = [[0] * n] * m # doesn't work
    # c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # correct
    c = [[(0) for _ in range(n)] for _ in range(m)]
    print(a)
    print(b)
    print(c, len(c), len(c[0]))
    for i in range(m):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
            # print(a[i][j] + b[i][j], c[i][j])

    for res in c:
        print(res)


# Using List Comphrension Technique
def mat_add2(a, b):
    m = len(a)
    n = len(b[0])
    print(a)
    print(b)
    for i in range(m):
        for j in range(n):
            c = [[a[i][j] + b[i][j] for j in range(n)] for i in range(m)]

    for res in c:
        print(res)


if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    mat_add(a, b)
    mat_add2(a, b)  # Recommended : Using List Comphrension Technique

    a = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
    b = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]
    mat_add(a, b)
    mat_add2(a, b)  # Recommended : Using List Comphrension Technique
