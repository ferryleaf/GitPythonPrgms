'''
given an Array of n integers, We are given q queries having indices l and r.
We have to find out sum between the given range of indices.

Input
[4, 5, 3, 2, 5]
3
0 3
2 4
1 3
Output
14 (4+5+3+2)
10 (3+2+5)
10 (5+3+2)

This is not SLIDING WINDOW PROBLEM.

SOLUTION:
prefix[] = Array stores the sum (A[0]+A[1]+....A[i]) at index i.
if l == 0 :
    sum(l,r) = prefix[r]
else :
    sum(l,r) = prefix[r] - prefix[l-1]

'''


def range_sum_query(arr, l, r):
    prefix_sum = []
    sum = 0
    for ele in arr:
        sum += ele
        prefix_sum.append(sum)

    if l == 0:
        return prefix_sum[r]
    else:
        return prefix_sum[r] - prefix_sum[l-1]


if __name__ == '__main__':
    '''
    arr = list(map(int, input().rstrip().split())
    T = int(input())
    for i in range(T):
        l, r = list(map(int, input().rstrip().split(,))
        print(range_sum_query(arr, l, r), end=" ")
    '''
    print(range_sum_query([4, 5, 3, 2, 5], 0, 3), end=" ")
    print(range_sum_query([4, 5, 3, 2, 5], 2, 4), end=" ")
    print(range_sum_query([4, 5, 3, 2, 5], 1, 3), end=" ")
