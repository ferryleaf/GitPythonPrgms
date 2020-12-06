'''
Given an array of integers of size 'n'.
Our aim is to calculate the maximum sum of 'k'
consecutive elements in the array.

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23}
of size 4.

Input  : arr[] = {2, 3}
         k = 3
Output : Invalid
There is no subarray of size 3 as size of whole
array is 2.
'''


def max_sum(arr, window_sze):
    # arr = [100, 200, 300, 400]
    # window_sze = 2
    window_start_idx = max_sum = 0
    window_end_idx = window_sze - 1

    for i in range(window_end_idx + 1):
        max_sum += arr[i]
    sum = max_sum

    while(window_end_idx < len(arr)-1):
        sum += arr[window_end_idx+1]
        sum -= arr[window_start_idx]
        window_end_idx += 1
        window_start_idx += 1
        if max_sum <= sum:
            max_sum = sum
    return max_sum


if __name__ == '__main__':
    # arr = list(map(input().rstrip().split(), int))
    # window_sze = int(input())
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    window_sze = 4
    print("Max Sum:", max_sum(arr, window_sze))

    arr = [100, 200, 300, 400]
    window_sze = 2
    print("Max Sum:", max_sum(arr, window_sze))
