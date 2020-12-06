'''
Microsoft

You are given an array of integers in an arbitrary order.
Return whether or not it is possible to make the array non-decreasing
by modifying at most 1 element to any value.

We define an array is non-decreasing
if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example:

[13, 4, 7] should return true, since we can modify 13 to any value 4 or less,
to make it non-decreasing.

[13, 4, 1] however, should return false,
since there is no way to modify just one element to make the array non-decreasing.

Can you find a solution in O(n) time?
'''

def check(lst):
    counter=0
    for i in range(0,len(lst)-1):
        if (lst[i]>lst[i+1]):
            counter+=1
        if (lst[i]==lst[i+1] and counter>=0):
            counter+=1

    if(counter==1):
        print('True')
    else:
        print('False')


if __name__=='__main__':
    check([13, 4, 7])
    check([13, 4, 1])
    check([13, 13, 1, 4])
    check([13, 4, 7, 7])
    check([13, 13, 4, 7, 7])
    check([1, 4, 7, 7])
    check([4, 4, 7, 7])
    check([5,1,3,2,5])
