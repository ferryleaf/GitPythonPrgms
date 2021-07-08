'''
Given an array arr[] of positive integers of size N. Reverse every sub-array
group of size K.

Example 1:

Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First group consists of elements
1, 2, 3. Second group consists of 4,5.

Example 2:

Input:
N = 4, K = 3
arr[] = {5,6,8,9}
Output: 8 6 5 9

Your Task:
You don't need to read input or print anything. The task is to complete the
function reverseInGroups() which takes the array, N and K as input parameters
and modifies the array in-place.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N, K ≤ 107
1 ≤ A[i] ≤ 1018
'''


class Solution:
    def reverseInGroups(self, arr, N, K):
        for i in range(0, N, K):
            if i+K-1 <= N:
                print(arr, i, i+K-1)
                reverse(arr, i, i+K-1)
            else:
                print(arr, i, N-1)
                reverse(arr, i, N-1)
        return


def reverse(arr, st, en):
    while(st < en):
        temp = arr[st]
        arr[st] = arr[en]
        arr[en] = temp
        st += 1
        en -= 1
    return


if __name__ == '__main__':
    # N = int(input())
    # K = int(input())
    ob = Solution()
    arr = [5, 6, 8, 9]
    print("before", arr)
    ob.reverseInGroups(arr, 4, 3)

    for i in arr:
        print(i, end=" ")
    print()

    arr = [36, 93, 64, 48, 96, 55, 70, 0, 82, 30, 16, 22, 38,
           53, 19, 50, 91, 43, 70, 88, 10, 57, 14, 94, 13, 36,
           59, 32, 54, 58, 18, 82, 67]
    Solution().reverseInGroups(arr, 33, 13)
    for i in arr:
        print(i, end=" ")
    print()
