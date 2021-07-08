''''''
Geek has drawn two lines parallel to each other and marked N points on each of them. After that, he drew N lines connecting N points on line 1 with N points on line 2. Each point on line 1 can be connected to exactly one point on line 2.
Find the largest group of lines such that each line in that group intersects the remaining lines.

Input:
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.

The first line of each test case contains an integer N.
Next N lines contains two space-separated integers representing the starting and ending marked point of N lines on two parallel lines.
Output:
For each test case, in a new line, print the answer.

Constraints:
1 ≤ T ≤ 1000
1 ≤ N ≤ 105
Sum of N in all testcases does not exceed 106
Each marked point is numbered from 1 to N


Example:

Sample Input:
2
5
1 4
4 3
3 5
5 1
2 2
2
1 2
2 1

Sample Output:
3
2

Explanation:
Test Case 1: First (1-4), Fourth(5-1), Fifth(2-2) are the three lines which are intersecting each other.

https://practice.geeksforgeeks.org/contest-problem/geek-and-lines/0/

'''
