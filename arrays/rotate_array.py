'''
Given an unsorted array arr[] of size N, rotate it by D elements
in the COUNTER CLOCKWISE DIRECTION.

Example 1:

Input:
N = 5, D = 2
arr[] = {1,2,3,4,5}
Output: 3 4 5 1 2
Explanation: 1 2 3 4 5  when rotated
by 2 elements, it becomes 3 4 5 1 2.

Example 2:

Input:
N = 10, D = 3
arr[] = {2,4,6,8,10,12,14,16,18,20}
Output: 8 10 12 14 16 18 20 2 4 6
Explanation: 2 4 6 8 10 12 14 16 18 20
when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.

Solution:
reverse(a, a+d) Reverse array from beginning till D
reverse(a+d, a+n) Reverse array from D till N
reverse(a, a+n) Reverse the whole array


UC 1:
77 69
40 13 27 87 95 40 96 71 35 79 68 2 98 3 18 93 53 57 2 81 87 42 66 90 45 20 41 30 32 18 98 72 82 76 10 28 68 57 98 54 87 66 7 84 20 25 29 72 33 30 4 20 71 69 9 16 41 50 97 24 19 46 47 52 22 56 80 89 65 29 42 51 94 1 35 65 25

Output:
29 42 51 94 1 35 65 25 40 13 27 87 95 40 96 71 35 79 68 2 98 3 18 93 53 57 2 81 87 42 66 90 45 20 41 30 32 18 98 72 82 76 10 28 68 57 98 54 87 66 7 84 20 25 29 72 33 30 4 20 71 69 9 16 41 50 97 24 19 46 47 52 22 56 80 89 65

UC 2:
5 2
1 2 3 4 5
Output: 3 4 5 1 2

UC3
10 3
2 4 6 8 10 12 14 16 18 20
Output: 8 10 12 14 16 18 20 2 4 6
'''

# More time consuming
def rotate_array(A, D, N):
    a = A[D-1::-1]
    b = A[N-1:D-1:-1]
    a = a + b
    return a[::-1]

# Faster
def rotateArr(A, D, N):
    temp = A[:D]
    for i in range(N):
        if i < N - D:
            A[i] = A[i + D]
        else:
            A[i] = temp[ i - (N - D)]



if __name__ == '__main__':
    # arr = list(map(input().rstrip().split()), int)
    arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    print(arr)
    print(rotate_array(arr, 3, 10))
    print(arr)
    print()

    arr = [1, 2, 3, 4, 5]
    print(arr)
    print(rotate_array(arr, 2, 5))
    print(arr)
