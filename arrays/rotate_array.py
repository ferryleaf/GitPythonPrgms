'''
Given an unsorted array arr[] of size N, rotate it by D elements
in the counter-clockwise direction.

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
'''


def rotate_array(A, D, N):
    a = A[D-1::-1]
    b = A[N-1:D-1:-1]
    a = a + b
    return a[::-1]


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
