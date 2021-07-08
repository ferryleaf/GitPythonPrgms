'''
given two sorted arrays arr1[ ] and arr2[ ] of size m and n respectively.
We have to merge these arrays and store the numbers in arr3[ ] of size m+n.
Input
1 3 4 6
2 5 7 8
Output
1 2 3 4 5 6 7 8

Input
1 2 5 9
3 7 8
Output
1 2 3 5 7 8 9

Input
1 2 5 9
3 7 10
Output
1 2 3 5 7 9 10

'''


def merge_sort(arr1, arr2):
    arr3 = []
    m = len(arr1)
    n = len(arr2)
    i = j = k = 0

    while ((i < m) & (j < n)):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
        k += 1

    while(k < m+n):
        if i == m:
            arr3.append(arr2[j])
            i += 1
        elif j == n:
            arr3.append(arr1[i])
            i += 1
        k += 1
    print(arr3)


def merge_sort2(arr1, arr2):
    arr3 = []
    m = len(arr1)
    n = len(arr2)
    i = j = 0
    while ((i < m) & (j < n)):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    while(i < m):
        arr3.append(arr1[i])
        i += 1

    while(j < n):
        arr3.append(arr1[i])
        i += 1


if __name__ == '__main__':
    merge_sort([1, 2, 5, 9], [3, 7, 8])
    merge_sort([1, 2, 5, 9], [3, 7, 10])
    merge_sort([1, 3, 4, 6], [2, 5, 7, 9])
