'''

https://practice.geeksforgeeks.org/tracks/dsa-workshop-1-matrix/?batchId=308
c
Videos: https://www.youtube.com/watch?v=1ZGJzvkcLsA
'''


def spiral_traversal(a):
    print()
    print(a)
    top = left = 0
    down = len(a) - 1
    right = len(a[0]) - 1
    direction = 0
    while(left <= right and top <= down):
        if direction == 0:
            # print()
            # print(direction)
            for i in range(left, right+1):
                print(a[top][i], end=" ")
            top += 1

        elif direction == 1:
            # print()
            # print(direction)
            for i in range(top, down+1):
                print(a[i][right], end=" ")
            right -= 1

        elif direction == 2:
            # print()
            # print(direction)
            for i in range(right, left-1, -1):
                print(a[down][i], end=" ")
            down -= 1

        elif direction == 3:
            # print()
            # print(direction)
            for i in range(down, top-1, -1):
                print(a[i][left], end=" ")
            left += 1
        direction = (direction + 1) % 4


if __name__ == '__main__':
    # Program to multiply two matrices using nested loops
    # 3x3 matrix
    a = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
    # [12, 7, 3, 6, 9, 8, 7, 4, 5]
    spiral_traversal(a)

    # 3x3 matrix
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # [1, 2, 3, 6, 9, 8, 7, 4, 5]
    spiral_traversal(a)

    # 3x4 matrix
    b = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]
    # [5, 8, 1, 2, 0, 1, 9, 5, 4, 6, 7, 3]
    spiral_traversal(b)
