


def selection_sort(arr):
    N = len(arr)
    for i in range(N-1):
        print("i:", i," arr:", arr)
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                val = arr[j]
                arr[j] = arr[i]
                arr[i] = val
    return arr

if __name__ == '__main__':
    arr = [5, 1, 4, 2, 8]
    print(arr, end= " ")
    print(selection_sort(arr))

    arr = [15, 13, 17, 8, 12]
    print(arr, end= " ")
    print(selection_sort(arr))

    arr = [15, 13, 17, 8, 4]
    print(arr, end= " ")
    print(selection_sort(arr))

    arr = [6, 7, 3, 2, 1, 9, 4]
    print(arr, end= " ")
    print(selection_sort(arr))

    arr = [2, 4, 1, 3, 5]
    print(arr, end= " ")
    print(selection_sort(arr))

    arr = [20, 12, 10, 15, 2]
    print(arr, end= " ")
    print(selection_sort(arr))
