'''
Given an array A of positive integers. Your task is to find the leaders in the
array. An element of array is leader if it is greater than or equal to all the
elements to its right side. The rightmost element is always a leader.


Example 1:

Input:
N = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17
as it is greater than all the elements
to its right.  Similarly, the next
leader is 5. The right most element
is always a leader so it is also
included.


Example 2:

Input:
N = 5
A[] = {1,2,3,4,0}
Output: 4 0


Your Task:
You don't need to read input or print anything.
The task is to complete the function leader() which takes array A and N as
input parameters and returns an array of leaders in order of their appearance.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)



Constraints:
1 <= N <= 107
0 <= Ai <= 107

'''


def leaders(A, N):
    # {16,17,4,3,5,2}    {17 5 2}
    # {16,17,5,4,3,2}    {17 5 4 3 2}
    # {18,18,16,17,5,4,3,2}    {18 18 17 5 4 3 2}
    # {18,17,4,3,5,2}    {18 17 5 2}
    # {1,2,3,4,0}        {4 0}
    max = A[N-1]
    lead = [A[N-1]]
    for i in range(N-2, -1, -1):
        if max <= A[i]:
            max = A[i]
            lead.append(max)

    return lead[::-1]


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().rstrip().split()))
    A = leaders(A, N)
    for ele in A:
        print(ele, end=" ")
