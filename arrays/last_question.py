'''
Given an array of positive integers of size N. The variation of the array is
given by the maximum difference between any two elements in the array.
Minimise the variation by performing the following operations on any element of
the array any number of times.

If the element is even, you can divide it by 2
If the element is odd, you can multiply it by 2
What will be the minimum variation after modifying the array ?

Input:
The first line of input contains the number of test cases T.
For each test case, the first line contains an integer N denoting the size of
the array and the second line contains N space-separated integers.


Output:
For each test case, in a new line, print the minimum variation of the array
after performing given operations.


Constraints:
1. 1  ≤ T  ≤ 100
2. 2  ≤ N  ≤ 104
3. 1  ≤ Elements of array  ≤ 106

Example:

Sample Input:
2
4
1 2 3 4
3
2 10 8

Sample Output:
1
3

Explanation:
Test Case 1: Transform [1,2,3,4] to [1,2,3,2] to [2,2,3,2]  then variation will
be (3-2)=1.

Test Case 2: Transform [2,10,8] to [2,5,4] then variation will be (5-2)=3.

https://practice.geeksforgeeks.org/contest-problem/the-last-question/0/
'''


def variation(arr, N):
    min = max = 2
    if N == 1:
        return 0

    for idx, ele in enumerate(arr):
        if (ele == 1) | (ele == 0):
            arr[idx] = 2
        else:
            while ele % 2 == 0:
                ele = ele // 2
            arr[idx] = ele
        if max < ele:
            max = ele
    print(min, max, arr)
    return (max - min)


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = list(map(int, input().rstrip().split()))
        print(variation(arr, N))
