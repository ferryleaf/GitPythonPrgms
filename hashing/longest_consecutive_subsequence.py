'''
Given an array A of integers. Find the length of the longest sub-sequence
such that elements in the sub-sequence are consecutive integers,
the consecutive numbers can be in any order.

Example 1:

Input:
7
1 9 3 10 4 20 2
Output:
4
Explanation:
Logest consecutive subsequence is 1, 2, 3, 4 of length 4.
Example 2:

Input:
11
36 41 56 35 44 33 34 92 43 32 42
Output:
5

Your task:
Complete findLongestConseqSubseq() function which takes both the given array
and their size as function arguments and returns the length of the longest
sub-sequence such that elements in the sub-sequence are consecutive integers.

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(N)

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= Ai <= 108
'''


def findLongestConseqSubseq(arr, n):
    sorted_arr = sorted(arr)
    print(sorted_arr)
    cnt = 1
    max_cnt = 1
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] - sorted_arr[i-1] == 1:
            cnt += 1
        else:
            if sorted_arr[i] - sorted_arr[i-1] != 0:
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 1
        if max_cnt < cnt:
            max_cnt = cnt
    return max_cnt


# Using Hashing
def findLongestConseqSubseq2(arr, n):
    mp = {x: 1 for x in arr}
    cnt = 1
    max_cnt = 1


if __name__ == '__main__':
    arr = [86, 77, 15, 93, 35, 86, 92, 49, 21, 62, 27, 90, 59, 63, 26, 40, 26,
    72, 36, 11, 68, 67, 29, 82, 30, 62, 23, 67, 35, 29, 2, 22, 58, 69, 67, 93,
    56, 11, 42, 29, 73, 21, 19, 84, 37, 98, 24, 15, 70, 13, 26, 91, 80, 56, 73,
    62, 70, 96, 81, 5, 25, 84, 27, 36, 5, 46, 29, 13, 57, 24, 95, 82, 45, 14,
    67, 34, 64, 43, 50, 87, 8, 76, 78, 88]
    print(findLongestConseqSubseq(arr, 84))

    arr = [1, 9, 3, 10, 4, 20, 2, 2]
    print(findLongestConseqSubseq(arr, 8))

    arr = [35, 57, 15, 56]
    print(findLongestConseqSubseq(arr, 4))
