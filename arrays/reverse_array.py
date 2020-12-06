'''
Given an array of n elements.
Reverse all the whole array.
'''


def reverse_array(arr):
    # return arr.reverse()
    return arr[::-1]


if __name__ == '__main__':
    arr = list(map(input().rstrip().split()), int)
    print(reverse_array(arr))
