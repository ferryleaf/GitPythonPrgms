'''
Given an array arr[] of size N, find the first repeating element.
The element should occurs more than once and the index of its first occurrence
should be the smallest.

Example 1:

Input:
N = 7
arr[] = {1, 5, 3, 4, 3, 5, 6}
Output: 2
Explanation:
5 is appearing twice and its first appearence is at index 2 which is less than
3 whose first occuring index is 3.

Example 2:

Input:
N = 4
arr[] = {1, 2, 3, 4}
Output: -1
Explanation:
All elements appear only once so answer is -1.

Your Task:
You don't need to read input or print anything. Complete the function
firstRepeated() which takes arr and N as input parameters and return the
position of the first repeating element. If there is no such element,return -1.
The position you return should be according to 1-based indexing.

Expected Time Complexity: O(NlogN)
Expected Auxilliary Space: O(N)


Constraints:
1 <= N <= 106
0 <= Ai<= 106
'''


def firstRepeated(arr, n):
    # arr : given array
    # n : size of the array
    if n == 1:
        return -1

    max = 0
    mp = dict()
    for idx, ele in enumerate(arr):
        if mp.get(ele) is not None:
            mp[ele] += 1
            if max < mp.get(ele):
                max = mp.get(ele)
        else:
            mp[ele] = 1

    for idx, ele in enumerate(arr):
        if (mp.get(ele) > 1) & (mp.get(ele) == max):
            return idx+1

    return -1


if __name__ == '__main__':
    print(firstRepeated[1, 2, 3, 4], 4)
    print(firstRepeated[1, 5, 3, 4, 3, 5, 6], 7)
    print(firstRepeated[1], 1)
