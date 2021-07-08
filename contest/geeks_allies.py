'''
Geek is a spy in an enemy town. There are N people in the town and every person has a unique natural number that denotes their identification. The ith person's identification code is i. His organisation has however, planted several allies in the town. They can be identified by their identification code as the digits in their codes form the smallest possible permutation. Given N, find out how many allies Geek has in the town.

Input:
First line of input contains number of testcases T.
For each testcase, there will a single input line containing N.

Output:
For each testcase, print how many allies Geek has in the town.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 9*1017

Example:

Sample Input:
2
13
500
Sample Output:
12
184
Explanation:
Testcase 1:
Identification codes of Geek's allies are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12
and 13. Person with Identification code 10 cannot be an ally as 10 is not the
smallest permutation of the digits '0' and '1'.

https://practice.geeksforgeeks.org/contest-problem/geek-and-allies/0/
'''
