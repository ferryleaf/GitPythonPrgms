'''
Search in a row wise and column wise sorted matrix
Last Updated: 23-10-2020
Given an n x n matrix and a number x,
find the position of x in the matrix if it is present in it.
Otherwise, print “Not Found”. In the given matrix, every row and column is
sorted in increasing order. The designed algorithm should have linear time
complexity.
Example:

Input: mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 29
Output: Found at (2, 1)
Explanation: Element at (2,1) is 29

Input : mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 100
Output : Element not found
Explanation: Element 100 is not found
'''


def mat_search(a, X):
    size = len(a)
    r = c = -1
    for i in range(size):
        if X >= a[0][i]:
            c = i
        if X >= a[i][0]:
            r = i
    for i in range(size):
        if a[r][i] == X:
            print(r, i, X)
            return
        if a[i][c] == X:
            print(i, c, X)
            return

    print("Not Found:", X)


if __name__ == '__main__':
    b = [[1, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
    mat_search(b, 29)
    mat_search(b, 5)
    mat_search(b, 100)
    mat_search(b, 27)
    mat_search(b, 45)
