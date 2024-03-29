'''
Given a positive integer N. The task is to check if N is a power of 2.
More formally, check if N can be expressed as 2x for some x.


Example 1:

Input: N = 1
Output: true
Explanation: 1 is equal to 2 raised to 0 (20 == 1).
Example 2:

Input: N = 98
Output: false
Explanation:
98 cannot be obtained by any power of 2.

Your Task: Your task is to complete the function isPowerofTwo() which takes n
as a parameter and returns true or false by checking is given number can be
represented as a power of two or not.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).
'''


def is_power_of_2(n):
    if n == 0:
        return 0
    if (n & (n-1)) == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    arr = [2, 4, 5, 6, 7, 8, 10, 12, 16]
    for ele in arr:
        print(ele, is_power_of_2(ele))
