'''
Given a non-empty array of integers, find the top K elements which have the
highest frequency in the array. If two numbers have the same frequency then
the larger number should be given preference.

Example 1:

Input:
N = 6
A[] = {1,1,1,2,2,3}
K = 2
Output: 1 2
Example 2:

Input:
N = 8
A[] = {1,1,2,2,3,3,3,4}
K = 2
Output: 3 2
Explanation: Elements 1 and 2 have the
same frequency ie. 2. Therefore, in this
case, the answer includes the element 2
as 2 > 1.
User Task:
The task is to complete the function TopK() that takes the array and integer K
as input and returns a list of top K frequent elements.

Expected Time Complexity : O(NlogN)
Expected Auxilliary Space : O(N)

Constraints:
1 <= N <= 103
1<=A[i]<=104

'''


def TopK(arr, n, k):
    # freq count
    mp = dict()
    for ele in arr:
        if ele in mp:
            mp[ele] = mp.get(ele) + 1
        else:
            mp[ele] = 1
    print("arr:", arr)
    print("mp:", mp)

    # sort dict by freq values
    # and then for each freq. values as key sorted descending order.
    mp_val = dict()
    for key, val in mp.items():
        if val in mp_val:
            mp_val.get(val).append(key)
        else:
            mp_val[val] = [key]
    print("mp_val:", mp_val)
    sorted_mp_val = sorted(mp_val.items(), key=lambda x: (x[0], x[1]), reverse=True)
    print("sorted_mp_val:", sorted_mp_val)
    cnt = 0
    for i in range(len(sorted_mp_val)):
        for j in range(len(sorted_mp_val[i][1])):
            print(sorted_mp_val[i][1][j], end=" ")
            if k == cnt:
                break
            cnt += 1


if __name__ == '__main__':
    # Output: 5,4 2
    arr = [4, 5, 5, 6, 4]
    print(arr, TopK(arr, 5, 2))

    '''

    # Output: 1 2
    arr = [1, 1, 1, 2, 2, 3]
    print(arr, TopK(arr, 6, 2))

    arr = [1, 1, 2, 2, 3, 3, 3, 4]
    TopK(arr, 8, 2)
    '''
