'''
Given a sorted array arr[] of distinct integers.
Sort the array into a wave-like array and return it. In other words,
arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....
(considering the increasing lexicographical order).

Example 1:

Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 2 1 4 3 5
Explanation: Array elements after sorting it in wave form are 2 1 4 3 5.


Example 2:

Input:
N = 6
arr[] = {2,4,7,8,9,10}
Output: 4 2 8 7 10 9
Explanation: Array elements after
sorting it in wave form are
4 2 8 7 10 9.
Your Task:
The task is to complete the function convertToWave() which converts the given
array to wave array.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 106
0 ≤ A[i] ≤107
'''


def convertToWave(A, N):
    if N == 1:
        return A

    for i in range(0, N-1, 2):
        if (A[i] < A[i+1]):
            temp = A[i]
            A[i] = A[i+1]
            A[i+1] = temp
    return A


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().rstrip().split()))
    convertToWave(A, N)
    for ele in A:
        print(ele, end=" ")
