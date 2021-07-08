'''
Given a sorted array arr[] of N elements, write a function to search a
given element X in arr[] using Binary Search Algorithm.
'''


def binary_search_iterative(arr, X):
    left = 0
    right = len(arr) - 1
    while(left <= right):
        mid = left + ((right - left) // 2)
        if arr[mid] == X:
            return mid
        if X < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def binary_search_recursive(arr, X, left, right):
    if left <= right:
        mid = left + ((right - left)//2)

        if arr[mid] == X:
            # print(mid)
            return mid

        if X < arr[mid]:
            return binary_search_recursive(arr, X, left, mid - 1)
        else:
            return binary_search_recursive(arr, X, mid + 1, right)

    return -1


if __name__ == '__main__':
    list_of_arrs = [([1, 2, 3, 4, 5, 6], 2),
                    ([1, 2, 3, 4, 5, 6, 7, 8], 8),
                    ([10, 20, 25, 30, 60, 65, 110, 120, 130, 170], 110),
                    ([10, 20, 25, 30, 60, 65, 110, 120, 130, 170], 175),
                    ([10, 20, 25, 30, 60, 65, 110, 120, 130, 170], 170),
                    ([10], 10),
                    ([10], 20)]

    for arr, X in list_of_arrs:
        print(arr, X, 1 + binary_search_recursive(arr, X, 0, len(arr)-1))
        print(arr, X, 1 + binary_search_iterative(arr, X))
