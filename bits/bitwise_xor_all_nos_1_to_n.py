'''
Given a number N, the task is to find the XOR of all numbers from 1 to N.

Examples :
Input : N = 6
Output : 7
// 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6  = 7

Input : N = 7
Output : 0
// 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 = 0
Solution:
Find the remainder of N by moduling it with 4.
If rem = 0, then xor will be same as N.
If rem = 1, then xor will be 1.
If rem = 2, then xor will be N+1.
If rem = 3 ,then xor will be 0.
'''
