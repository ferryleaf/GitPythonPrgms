'''
Insert an element in the array

'''


def insert_element(arr, ele, index):
    if index >= len(arr):
        arr.append(ele)
    else:
        v1 = arr[index]
        arr[index] = ele
        for i in range(index+1, len(arr)):
            v2 = arr[i]
            arr[i] = v1
            v1 = v2
            arr.append(v1)
    print(arr)


if __name__ == '__main__':
    arr = [15, 13, 17, 8, 4]
    print(arr)
    insert_element(arr, 5, 5)

    arr.insert(5, 745)
    print(arr)
    arr.insert(3, 55)
    print(arr)
