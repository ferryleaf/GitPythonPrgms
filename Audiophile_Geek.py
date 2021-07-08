'''
Geek is an Audiophile. He has a list of N different audios and he wishes to listen to M audios. He asks his friend Ted to create a playlist that satisfies two conditions.
1. Every audio should be played at least one time.
2. An audio can be played again only if K other audios have been played.
Find the total number of possible playlists that can be created by Ted.

Input:
The first line of input contains number of test cases T.
For each test case, there will be a single line of input that contains three space-separated integers N, M, and K.

Output:
For each test case, in a new line, print the total number of possible playlists created by Ted modulo 109 + 7.

Constraints:
1 ≤ T ≤ 1000
0 ≤ K < N ≤ M ≤ 100

Example:

Sample Input:
3
3 3 1
2 3 0
2 3 1
Sample Output:
6
6
2
Explanation:
Test Case 1: Possible Playlists are:
[1, 2, 3], [1, 3, 2], [2, 1, 3],
[2, 3, 1], [3, 1, 2] and [3, 2, 1].
Test Case 2: Possible Playlists are:
[1, 1, 2], [1, 2, 1], [2, 1, 1],
[2, 2, 1], [2, 1, 2] and [1, 2, 2].
Test Case 3: Possible Playlists are:
[1, 2, 1] and [2, 1, 2].
https://practice.geeksforgeeks.org/contest-problem/audiophile-geek/0/

'''
