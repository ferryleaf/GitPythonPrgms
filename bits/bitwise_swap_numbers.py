'''
swap two numbers say a and b by using the XOR(^) operator by applying below
operations:

'''


def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b


if __name__ == '__main__':
    print(swap(15, 8))
    print(swap(55, 8))
