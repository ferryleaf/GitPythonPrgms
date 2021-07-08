'''
Geek lives in a special city where houses are arranged in a hierarchial tree-like manner. Starting from house number 1, each house leads to two more houses. If you read the house numbers in level-order format, you get 1, 2, 3, 4, 5......and so on. ie- all the natural numbers arranged in ascending order .
Given the house numbers of two houses x and y, find the length of the shortest path between them.

Input:
First line of input contains number of testcases T. For each testcase, there will a single line of input containing two space separated integers x and y.

Output:
For each testcase, in a new line, print the length of the shortest path between x and y.

Constraints:
1. 1 ≤ T ≤ 100
2. 1 ≤ x,y ≤ 109

Example:

Sample Input:
2
2 6
8 10

Sample Output:
3
4

Explanation:

             1
          /      \
       2             3
     /   \         /   \
    4     5       6     7
   / \   / \     / \   / \
  8  9  10 11   12 13 14 15

Testcase 1: 2-> 1-> 3-> 6
The length of the shortest path between 2 and 6 is 3.

Testcase 2: 8-> 4-> 2-> 5-> 10
The length of the shortest path between 8 and 10 is 4.

https://practice.geeksforgeeks.org/contest-problem/hierarchical-city-links/0/

'''
