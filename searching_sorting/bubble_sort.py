'''
Bubble Sort is also an in-place sorting algorithm. This is the simplest
sorting algorithm and it works on the principle that:
In one iteration if we swap all adjacent elements of an array such that after
swap the first element is less than the second element then at the end of the
iteration, the first element of the array will be the minimum element.

Bubble-Sort algorithm simply repeats the above steps N-1 times, where N is the
size of the array.

Example: Consider the array, arr[] = {5, 1, 4, 2, 8}.
First Pass: ( 5 1 4 2 8 ) --> ( 1 5 4 2 8 ), Here, algorithm compares the first
two elements, and swaps since 5 > 1.
( 1 5 4 2 8 ) -->  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) -->  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) --> ( 1 4 2 5 8 ), Now, since these elements are already in order
(8 > 5), algorithm does not swap them.
Second Pass: ( 1 4 2 5 8 ) --> ( 1 4 2 5 8 )
( 1 4 2 5 8 ) --> ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 ) --> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) -->  ( 1 2 4 5 8 )
Now, the array is already sorted, but our algorithm does not know if it is
completed. The algorithm needs one whole pass without any swap to know it is
sorted.

Third Pass: ( 1 2 4 5 8 ) --> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) --> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) --> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) --> ( 1 2 4 5 8 )
'''


def bubble_sort(arr):
    N = len(arr)
    for i in range(N-1):
        for j in range(N-i-1):
            if arr[j] > arr[j+1]:
                val = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = val
            print("i:", i," arr:", arr)
    return arr


if __name__ == '__main__':
    # arr = [5, 1, 4, 2, 8]
    # print(arr)
    # print(bubble_sort(arr))
    #
    # arr = [15, 13, 17, 8, 12]
    # print(arr)
    # print(bubble_sort(arr))

    arr = [15, 13, 17, 8, 4]
    print(arr)
    print(bubble_sort(arr))
