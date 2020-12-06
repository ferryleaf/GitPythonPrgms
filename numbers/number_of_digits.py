'''
Given an integral number N. The task is to find the count of digits present
in this number.

Let's say:
N = 2019

Number of digits in N here is 4 and,
the digits are: 2, 0, 1, 9.

Some more Examples:
N = 1567
Number of digits = 4

N = 256
Number of digits = 3

N = 58964
Number of digits = 5
'''


def number_of_digits(num):
    temp = num
    cnt = 0
    while(int(temp/10) != 0):
        cnt += 1
        temp = int(temp/10)
    print("Num of digits:", cnt+1)


def number_of_digits_app2(num):
    import numpy as np
    print("Num of digits:", int(np.log10(num))+1)


if __name__ == '__main__':
    num = int(input().rstrip())
    number_of_digits(int(num))
    number_of_digits_app2(int(num))
