'''
Given an array arr[] of size N, find the smallest positive number missing from the array.


N = 5
arr[] = {0,-10,1,3,-20}
Output: 2

Your Task:
You don't need to read input or print anything. The task is to complete the
function findMissing() which takes arr and N as input parameters and returns
the smallest positive missing number.

if len(arr)==1  return 1

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 <= N <= 106
-106 <= arr[i] <= 106
'''


def findMissing(arr, size):
    # your code goes here
    # if size of array= 1 the value could be 0 or -20 or 40
    # But 1 is the smallest positive number
    if len(arr) == 1:
        return 1

    min = max = 1
    mp = {}
    for ele in arr:
        if ele > 0:
            if max < ele:
                max = ele
            if min > ele:
                min = ele
            mp[ele] = ele

    for ele in range(min, max+1, 1):
        if mp.get(ele) is None:
            return ele
    return max+1


def firstMissingPositive_2(arr, n):
    ptr = 0
    # Check if 1 is present in array or not
    for i in range(n):
        if arr[i] == 1:
            ptr = 1
            break

    # If 1 is not present
    if ptr == 0:
        return(1)

    # Changing values to 1
    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = 1

    # Updating indices according to values
    for i in range(n):
        arr[(arr[i] - 1) % n] += n

    # Finding which index has value less than n
    for i in range(n):
        if arr[i] <= n:
            return(i + 1)

    # If array has values from 1 to n
    return(n + 1)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(findMissing(arr, 5))
    arr = [0, -10, 1, 3, -20]
    print(findMissing(arr, 5))
