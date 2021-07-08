'''
Given two numbers M and N. The task is to find the position of the rightmost
different bit in the binary representation of numbers.

Example 1:

Input: M = 11, N = 9
Output: 2
Explanation: Binary representation of the given
numbers are: 1011 and 1001,
2nd bit from right is different.
Example 2:

Input: M = 52, N = 4
Output: 5
Explanation: Binary representation of the given
numbers are: 110100â€¬ and 0100,
5th-bit from right is different.
User Task:
The task is to complete the function posOfRightMostDiffBit() which takes two
arguments m and n and returns the position of first different bits in m and n.
If both m and n are the same then return -1 in this case.

Expected Time Complexity: O(max(log m, log n)).
Expected Auxiliary Space: O(1).

Constraints:
1 <= M <= 103
1 <= N <= 103


'''


# 0.02 secs
def posOfRightMostDiffBit(m, n):
    if m == n:
        return -1

    cnt = 1
    i = 0
    while((((m >> i) & 1) ^ ((n >> i) & 1)) == 0):
        print(bin(m), bin(n))
        m = m >> i
        n = n >> i
        cnt += 1
        i = 1
    return cnt


if __name__ == '__main__':
    print(posOfRightMostDiffBit(9, 9))
    print(posOfRightMostDiffBit(52, 4))
    print(posOfRightMostDiffBit(11, 9))
