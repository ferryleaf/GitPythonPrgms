'''
Largest subarray with 0 sum
Given an array having both positive and negative integers.
The task is to compute the length of the largest subarray with sum 0.

Example 1:

Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.
Your Task:
You just have to complete the function maxLen() which takes two arguments an
array A and n, where n is the size of the array A and returns the length of the
largest subarray with 0 sum.

Expected Time Complexity: O(N*Log(N)).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 104
-1000 <= A[i] <= 1000, for each valid i
'''


def maxLen(n, arr):
    # NOTE: Dictonary in python in implemented as Hash Maps
    # Create an empty hash map (dictionary)
    hash_map = {}

    # Initialize result
    max_len = 0

    # Initialize sum of elements
    curr_sum = 0

    # Traverse through the given array
    for i in range(len(arr)):

        # Add the current element to the sum
        curr_sum += arr[i]

        if arr[i] is 0 and max_len is 0:
            max_len = 1

        if curr_sum is 0:
            max_len = i + 1

        # NOTE: 'in' operation in dictionary to search
        # key takes O(1). Look if current sum is seen
        # before
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:

            # else put this sum in dictionary
            hash_map[curr_sum] = i
        # print(max_len)
    return max_len


def maxLen2(n, arr):
    sum = 0
    sum_mp = dict()
    lar_arr = 0
    for idx, ele in enumerate(arr):
        sum += ele

        if lar_arr == 0 and ele == 0:
            lar_arr == 1

        # if ith cell is 0, which means starting from length of largest
        # array: 0 to ith cell
        # largest array =  0 to idx or idx + 1
        if sum == 0:
            lar_arr = idx + 1

        if sum in sum_mp:
            sum_mp[sum] = idx - sum_mp.get(sum)
            if lar_arr < sum_mp.get(sum):
                lar_arr = sum_mp.get(sum)
        else:
            sum_mp[sum] = idx
    return lar_arr


if __name__ == '__main__':
    # Ans:
    arr = [15, -2, 2, -8, 1, 7, 10, 23]
    print(arr, maxLen(8, arr))
    print(arr, maxLen2(8, arr))

    # Ans: 4
    arr = [-1, 1, -1, 1]
    print(arr, maxLen(4, arr))
    print(arr, maxLen2(4, arr))

    # Ans: 1
    arr = [0, 15, -2, 3]
    print(arr, maxLen(4, arr))
    print(arr, maxLen2(4, arr))

    # Ans: 0
    arr = [8, 0, 15, -2, 3]
    print(arr, maxLen(4, arr))
    print(arr, maxLen2(4, arr))


    # Ans 3
    arr = [-776, 794, 387, -648, 363, 691, 764, -539, -171, -210, -566, 783,
    -861, 68, 930, -21, -68, 394, -10, -228, 422, 785, 199, -314, -412, -90,
    -955, 863, -995, 306, 85, 337, 847, 314, 125, 583, 815, 435, -42, -86,
    -275, -787, -402, 755, 933, -675, -738, -225, -93, 796, -433, -466, 98,
    -316, -651, -300, -285, 866, 445, 441, 32, 98, 482, 710, 568, -496, 587,
    307, 220, -527, 733, 504, 271, -707, 341, 797, 619, 847, 922, 380, -763,
    -840, -192, -33]
    print(arr, maxLen(84, arr))
    print(arr, maxLen2(84, arr))
