'''
Given a binary string S, the task is to move all the zeros to the front in the minimum possible time. In one second, you can swap all zero-one pairs where 1 is present on the adjacent left of 0.
ie - if one is at the ith position and zero at (i+1)th position, they can be swapped.

Input:
The first line of the input contains a single integer T denoting the number of test cases. The first line of each test case contains a binary string S.

Output:
For each test case, in a new line, print the minimum seconds required to modify the string as suggested above.

Constraints:
1 ≤ T ≤ 100
1 ≤ |S| ≤ 105


Example:

Sample Input:
2
1100
001

Sample Output:
3
0

Explanation:
Test Case 1 : "1100" -> "1010" -> "0101" -> "0011"

https://practice.geeksforgeeks.org/contest-problem/binary-numbers5602/0/
'''
