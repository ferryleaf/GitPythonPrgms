'''
Problem:
Given an array arr[] of N elements, write a function to search a
given element X in arr[].

Input : arr[] = {10, 20, 80, 30, 60, 50, 110, 100, 130, 170}
        key = 110;
Output : 6
Element 110 is present at index 6

Input : arr[] = {10, 20, 80, 30, 60, 50, 110, 100, 130, 170}
        key = 175;
Output : -1
Element 175 is not present in arr[].

'''


def linear_search(arr, key):
    # returns index of the key in arr
    i = -1
    for idx, ele in enumerate(arr):
        if key == ele:
            return idx
    return i


if __name__ == '__main__':
    print(linear_search([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], 110))
    print(linear_search([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], 175))
    print(linear_search([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], 170))
    print(linear_search([10], 10))
    print(linear_search([10], 20))
