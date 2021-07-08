'''
Hashing is very useful to keep track of the frequency of the elements in list.

You are given an array of integers. You need to print the non-repeated elements
as they appear in the array.

Example 1:

Input:
n = 10
arr[] = {1,1,2,2,3,3,4,5,6,7}
Output: 4 5 6 7
Explanation: 4, 5, 6 and 7 are the only
elements which is having only 1
frequency and hence, Non-repeating.
Example 2:

Input:
n = 5
arr[] = {10,20,40,30,10}
Output: 20 40 30
Explanation: 20, 40, 30 are the only
elements which is having only 1
frequency and hence, Non-repeating.
Your Task:
You don't need to read input or print anything. You only need to complete the
function printNonRepeated() that takes arr and n as parameters and return
the array which has the distinct elements in same order as they appear in
input array. The newline is appended automatically by the driver code.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Constraints:
1 <= n <= 103
0 <= arri <= 107

'''


def printNonRepeated(arr, n):
    mp = dict()
    for ele in arr:
        if mp.get(ele):
            mp[ele] = mp.get(ele) + 1
        else:
            mp[ele] = 1

    arr_new = []
    for ele in arr:
        if mp.get(ele) == 1:
            arr_new.append(ele)

    return arr_new


def printNonRepeated2(arr, n):
    mp_new = dict()
    mp = dict()
    for ele in arr:
        if mp.get(ele):
            mp[ele] = mp.get(ele) + 1
            mp_new.pop(ele)
        else:
            mp[ele] = 1
            mp_new[ele] = 1
    return mp_new.keys()


if __name__ == '__main__':
    print(printNonRepeated([1, 1, 2, 2, 3, 3, 4, 5, 6, 7], 10))
    print(printNonRepeated([10, 20, 40, 30, 10], 5))
    print(printNonRepeated2([1, 1, 2, 2, 3, 3, 4, 5, 6, 7], 10))
    print(printNonRepeated2([10, 20, 40, 30, 10], 5))
