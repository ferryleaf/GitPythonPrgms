'''
Given an array arr[] of size N, the task is to generate the prefix sum array
of the given array.

Prefix Sum Array: The prefix sum array of any array, arr[] is defined as an
array of same size say, prefixSum[] such that the value at any index i in
prefixSum[] is sum of all elements from indexes 0 to i in arr[].

That is,
prefixSum[i] = arr[0] + arr[1] + arr[2] + . . . . + arr[i]

for all 0 <= i <= N.
'''


def fillPrefixSum(arr):
    prefixSum = list()
    prefixSum.append(arr[0])
    for i in range(1, len(arr)):
        prefixSum.append(prefixSum[i-1] + arr[i])
    return prefixSum


if __name__ == '__main__':
    arr = [100, 200, 300, 400]
    print("Original Array", arr)
    print("prefixSum:", fillPrefixSum(arr))
