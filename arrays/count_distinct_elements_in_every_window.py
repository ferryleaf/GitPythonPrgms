'''
Given an array of integers and a number K. Find the count of distinct elements
in every window of size K in the array.

Example 1:

Input:
N = 7, K = 4
A[] = {1,2,1,3,4,2,3}
Output: 3 4 4 3
Explanation: Window 1 of size k = 4 is
1 2 1 3. Number of distinct elements in
this window are 3.
Window 2 of size k = 4 is 2 1 3 4. Number
of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number
of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number
of distinct elements in this window are 3.
Example 2:

Input:
N = 3, K = 2
A[] = {4,1,1}
Output: 2 1
Your Task:
Your task is to complete the function countDistinct() which takes the array A[]
the size of the array(N) and the window size(K) as inputs and returns an array
containing the count of distinct elements in every contiguous window of size K
in the array A[].

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= K <= 105
1 <= A[i] <= 105 , for each valid i
'''


def countDistinct(arr, N, K):
    # Execution Time: 3.65
    res = []
    for j in range(N-K+1):
        mp = dict()
        sub_arr = arr[j:j+K]
        mp = dict(zip(sub_arr, sub_arr))
        res.append(len(mp))
    return res


def countDistinct2(arr, N, K):
    # Execution Time:1.68
    res = []
    mp = dict()
    for i in range(K):
        if mp.get(arr[i]) is None:
            mp[arr[i]] = 1
        else:
            mp[arr[i]] = mp.get(arr[i]) + 1
    res.append(len(mp))

    start = 0
    end = K
    while end < N:
        if mp.get(arr[start]) is not None:
            mp[arr[start]] = mp.get(arr[start]) - 1
            if mp.get(arr[start]) == 0:
                mp.pop(arr[start])
        start += 1
        if mp.get(arr[end]) is None:
            mp[arr[end]] = 1
        else:
            mp[arr[end]] = mp.get(arr[end]) + 1
        res.append(len(mp))
        end += 1
    return res


if __name__ == '__main__':
    N = int(input())
    K = int(input())
    arr = list(map(int, input().rstrip().split(' ')))
    res = countDistinct2(arr, N, K)
    for i in res:
        print(i, end=" ")
