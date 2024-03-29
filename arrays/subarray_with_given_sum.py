'''
Given an unsorted array A of size N that contains only non-negative integers,
find a continuous sub-array which adds to a given number S.



Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements
from 2nd position to 4th position
is 12.


Example 2:

Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements
from 1st position to 5th position
is 15.


Your Task:
You don't need to read input or print anything. The task is to complete the
function subarraySum() which takes arr, N and S as input parameters and returns
a list containing the starting and ending positions of the first such occurring
subarray from the left where sum equals to S. The two indexes in the list
should be according to 1-based indexing. If no such subarray is found,
return -1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)



Constraints:
1 <= N <= 105
1 <= Ai <= 1010



Constraints:
1 <= n <= 105
1 <= Ai <= 1010
# n = 5, S = 12, A[] = {1,2,3,7,5}              2 4
# n = 5, S = 12, A[] = {1,2,3,4,5}              3 5
# n = 5, S = 13, A[] = {1,2,3,4,5}              -1
# n = 10, S = 15, A[] = {1,2,3,4,5,6,7,8,9,10}  1 5
# n = 10, S = 20, A[] = {1,2,3,4,5,6,7,8,9,10}  2 6
# n = 6, S = 33, A[] = {1,4,20,3,10,5}          3 5
'''


def subArraySum(arr, n, sum):
    start = end = 0
    max_sum = arr[0]
    if max_sum == sum:
        print(start+1, end+1)

    while start < n-1:
        if (max_sum < sum):
            if (end < n-1):
                end += 1
                max_sum += arr[end]
            else:
                start += 1

        if max_sum > sum:
            max_sum -= arr[start]
            start += 1

        if max_sum == sum:
            print(start+1, end+1)
            break

    if (end == n-1) & (max_sum != sum):
        print(-1)


if __name__ == '__main__':
    n = int(input())
    sum = int(input())
    arr = list(map(int, input().rstrip().split(',')))
    subArraySum(arr, n, sum)
