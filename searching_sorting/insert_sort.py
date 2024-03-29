'''
Insertion Sort is an In-Place sorting algorithm. This algorithm works in a
similar way of sorting a deck of playing cards.

The idea is to start iterating from the second element of array till last
element and for every element insert at its correct position in the subarray
before it.

Another Example:
arr[] = {12, 11, 13, 5, 6}

Let's loop for i = 1 (second element of the array) to 4 (Size of input array-1)
i = 1, Since 11 is smaller than 12, move 12 and insert 11 before 12.
11, 12, 13, 5, 6
i = 2, 13 will remain at its position as all elements in A[0..I-1] are smaller
than 13

11, 12, 13, 5, 6
i = 3, 5 will move to the beginning and all other elements from 11 to 13 will
move one position ahead of their current position.
5, 11, 12, 13, 6
i = 4, 6 will move to position after 5, and elements from 11 to 13 will move
one position ahead of their current position.
5, 6, 11, 12, 13
'''

def insert_sort(arr):
    N = len(arr)
    for i in range(N):
        for j in range(i):
            print("i:", i," j:", j," arr:", arr)
            if arr[i] < arr[j]:
                arr.insert(j, arr[i])
                arr.pop(i+1)
                break
    return arr

if __name__ == '__main__':
    arr = [4, 3, 2, 10, 12, 1, 5, 6]
    print(arr)
    print(insert_sort(arr))

    arr = [5, 1, 4, 2, 8]
    print(arr)
    print(insert_sort(arr))

    arr = [15, 13, 17, 8, 12]
    print(arr)
    print(insert_sort(arr))

    arr = [15, 13, 17, 8, 4]
    print(arr)
    print(insert_sort(arr))
