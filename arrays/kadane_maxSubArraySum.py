'''
Largest Sum Contiguous Subarray
[Write an efficient program to find the sum of contiguous subarray within a
one-dimensional array of numbers which has the largest sum.]

Given an array arr of N integers.
Find the contiguous sub-array with maximum sum.

Example 1:

Input:
N = 5
arr[] = {1,2,3,-2,5}
Output: 9
Explanation: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which
is a contiguous subarray.


Example 2:

Input:
N = 4
arr[] = {-1,-2,-3,-4}
Output: -1
Explanation: Max subarray sum is -1 of element (-1)


Your Task:
You don't need to read input or print anything. The task is to complete the
function maxSubarraySum() which takes arr and N as input parameters and
returns the sum of subarray with maximum sum.



Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)



Constraints:
1 ≤ N ≤ 106
-107 ≤ A[i] <= 107

Input:
8
-47 43 94 -94 -93 -59 31 -86

Its Correct output is:
137

And Your Code's output is:
94
'''


def maxSubArraySum(a, size):
    max_sum = max_sum_so_far = min_sum = flag = 0
    for i in range(size):
        max_sum_so_far += a[i]
        if a[i] == 0:
            flag = 1

        if max_sum < max_sum_so_far:
            max_sum = max_sum_so_far

        if max_sum_so_far < 0:
            if (min_sum == 0):
                min_sum = max_sum_so_far
            else:
                if min_sum < max_sum_so_far:
                    min_sum = max_sum_so_far
            max_sum_so_far = 0

    if (max_sum == 0) & (min_sum != 0):
        if flag == 1:
            return 0
        else:
            return min_sum
    else:
        return max_sum


if __name__ == '__main__':
    # size = int(input())
    # a = list(map(int, input().rstrip().split()))
    # maxSubArraySum(a, size)
    print(maxSubArraySum([-47, 43, 94, -94, -93, -59, 31, -86], 8))  # 137
    print(maxSubArraySum([1, 2, 3, -2, 5], 5))  # 9
    print(maxSubArraySum([-1, -2, -3, -4], 4))  # -1
    print(maxSubArraySum([-2, -3, -4], 3))      # -2
    print(maxSubArraySum([-1, -2, 3, -4], 4))   # 3
    print(maxSubArraySum([-4, -3, -2, -5, -1], 5))  # -1
    print(maxSubArraySum([0, -1, 0, -1, 0, -1, 0, -1], 8))  # 0
