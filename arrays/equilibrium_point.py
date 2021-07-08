'''
Given an array A of N positive numbers. The task is to find the first
Equilibium Point in the array.

Equilibrium Point in an array is a position such that the sum of elements
before it is equal to the sum of elements after it.

Example 1:

Input:
N = 1
A[] = {1}
Output: 1
Explanation: Since its the only
element hence its the only equilibrium
point.
Example 2:

Input:
N = 5
A[] = {1,3,5,2,2}
Output: 3
Explanation: For second test case
equilibrium point is at position 3
as elements before it (1+3) =
elements after it (2+2).


Your Task:
The task is to complete the function equilibriumPoint() which takes the array
and N as input parameters and returns the point of equilibrium.
Return -1 if no such point exists.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 106
1 <= A[i] <= 108


Use Case:
# 1 3 5 2 2
# 2 2 5 2 9
# 2 2 5 2 8 1

'''


def equilibriumPoint(A, N):
    # Your code here
    if len(A) == 1:
        return 1

    before = A[0]
    after = 0
    for i in range(N-1, 1, -1):
        after += A[i]

    if before == after:
        return 1

    for i in range(2, N-1):
        before += A[i-1]
        after -= A[i]
        if before == after:
            return i+1

    return -1


if __name__ == '__main__':
    print(equilibriumPoint([1, 3, 5, 2, 2], 5))
    print(equilibriumPoint([2, 2, 5, 2, 9], 5))
    print(equilibriumPoint([1, 3, 5, 2, 8, 1], 6))
