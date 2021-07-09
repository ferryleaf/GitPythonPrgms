'''
Given a sorted array A of size N, delete all the duplicates elements from A.

Example 1:

Input:
N = 5
Array = {2, 2, 2, 2, 2}
Output: 2
Explanation: After removing all the duplicates
only one instance of 2 will remain.

Example 2:

Input:
N = 3
Array = {1, 2, 2}
Output: 1 2

Your Task:
You dont need to read input or print anything. Complete the function
remove_duplicate() which takes the array A[] and its size N as input parameters
and modifies it in place to delete all the duplicates. The function must return
an integer X denoting the new modified size of the array.

Note: The generated output will print all the elements of the modified array
from index 0 to X-1.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 <= N <= 104
1 <= A[i] <= 106


UC 1 : 1 6 6 8 9 10 : 1 6 8 9 10
UC 2 : 6 6 : 6
UC 3 : 1 : 1
UC 4 : 1 2 : 1 2
UC 5 : 1 3 4 4 : 1 3 4
UC 6 : 2 2 2 2 2 : 2
'''


class Solution:
    def remove_duplicate(self, A, N):
        if N != 1 and N != 0:
            i = 0
            n = A[i]
            while n is not None:
                if i < len(A)-1 and A[i] == A[i+1]:
                    A.pop(i+1)
                else:
                    i+=1
                    if i >= len(A):
                        n = None
                    else:
                        n = A[i]
        return len(A)

if __name__ == '__main__':
    A = [2, 2, 2, 2, 2, 1, 3, 4, 5, 5, 7, 3, 6, 4, 4, 10]
    ob = Solution()
    print(A)
    n = ob.remove_duplicate(A, 16)
    for i in range(n):
        print(A[i], end=" ")
    print()
