'''
Given an array arr of length N consisting cost of toys.
Given an integer K depicting the amount with you. The task is to Maximise
the number of different toys you can have with K amount.

Example 1:

Input: N = 7, K = 50
arr = {1, 12, 5, 111, 200, 1000, 10}
Output: 4
Explaination: The costs of the toys are
1, 12, 5, 10.
Example 2:

Input: N = 3, K = 100
arr = {20, 30, 50}
Output: 3
Explaination: We can buy all types of
toys.
Your Task:
You do not need to read input or print anything. Your task is to complete the
function toyCount() which takes the value N, K and the array arr and
returns the maximum count of toys.

Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 1000
1 ≤ K, arr[i] ≤ 10000
'''


def toyCount(N, K, arr):
    arr.sort()
    sum = cnt = 0
    for ele in arr:
        if (sum + ele) <= K:
            sum += ele
            cnt += 1
        else:
            break
    return cnt


if __name__ == '__main__':
    print(toyCount(3, 100, [20, 30, 50]))
    print(toyCount(7, 50, [1, 12, 5, 111, 200, 1000, 10]))
