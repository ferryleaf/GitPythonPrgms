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


UC 1 :
6 3
1 2 3 4 5 6 ==> 3 2 1 6 5 4

UC2:
1 1
1 ==> 1

UC3:
2 1
1 2 ==> 1 2

UC4:
6 2
1 2 3 4 5 6 ==> 2 1 4 3 6 5

UC5:
3 1
1 2 3 ==> 1 2 3

UC6:
4 3
5 6 8 9 ==> 8 6 5 9

UC7:
1 0
1 ==> 1

UC8:
6 8
1 2 3 4 5 6 ==> 6 5 4 3 2 1
'''


class Solution:
    # Expected Time Complexity: O(N)
    # Expected Auxiliary Space: O(N) but completed it O(4) ==> O(1)
    def reverseInGroups(self, arr, N, K):
        if K == 0:
            return
        if K >= N:
            K = N
        i = 0
        k1 = k2 = K - 1
        while (i < N):
            if i < k2:
                temp = arr[k2]
                arr[k2] = arr[i]
                arr[i] = temp
                i+=1
                k2-=1
            else:
                i = k1 + 1
                k1 = k1 + K
                k2 = k1
                if k1 >= N:
                    k1 = k2 = N - 1
                if i >= N:
                    return

    def reverseInGroups2(self, arr, N, K):
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
