

def peakElement(arr, n):
    # Code here
    if n == 1:
        return 0

    for i in range(n):
        if i == 0:
            if arr[i] >= arr[i+1]:
                return i

        if i == n-1:
            if arr[i] >= arr[i-1]:
                return i

        if (arr[i] >= arr[i-1]) and (arr[i] >= arr[i+1]):
            return i


def peakElement2(arr, n):
    # Binary Search : [1, 4, 3, 5, 2]: [1, 2, 3, 4, 5]
    if n == 1:
        return 0

    for i in range(n):
        if i == 0:
            if arr[i] >= arr[i+1]:
                return i

        elif i == n-1:
            if arr[i] >= arr[i-1]:
                return i

        elif (arr[i] >= arr[i-1]) and (arr[i] >= arr[i+1]):
            return i


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    n = 5
    index = peakElement(arr, n)
    print(index)
    flag = False
    if index == 0 and n == 1:
        print('1')
        flag = True
    elif index == 0 and arr[index] >= arr[index+1]:
        print('2')
        flag = True
    elif index == n-1 and arr[index] >= arr[index-1]:
        print('3')
        flag = True
    elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
        print('4')
        flag = True
    else:
        flag = False

    '''
    print(peakElement([1, 2, 3], 3))  # 2
    print(peakElement([1, 3, 3], 3))  # 1
    print(peakElement([3, 2, 3], 3))  # 0
    print(peakElement([3, 2, 1], 3))  # 0
    print(peakElement([3, 2], 2))    # 0
    print(peakElement([2], 1))      # 0
    print(peakElement([2, 3], 2))    # 1
    '''

    '''
    print(peakElement([1, 2, 3, 5, 4], 5))  # 3
    print(peakElement([1, 2, 3, 5, 5], 5))  # 3
    '''
