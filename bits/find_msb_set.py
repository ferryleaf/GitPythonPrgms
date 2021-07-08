'''
Given a number N, find the most significant set bit in the given number.

Examples:
Input : N = 10
Output : 8
Binary representation of 10 is 1010
The most significant bit corresponds to decimal number 8.

Input : N = 18
Output : 16
Bitwise Solution: The most-significant bit in binary representation of a number
is the highest ordered bit, that is it is the bit-position with highest value.

One of the solution is first find the bit-position corresponding to the MSB in
the given number, this can be done by calculating logarithm base 2 of the given
number, i.e., log2(N) gives the position of the MSB in N.

Once, we know the position of the MSB, calculate the value corresponding to it
by raising 2 by the power of calculated position. That is, value = 2log2(N).
'''


def find_msb(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    i = 0
    while n > 1:
        i += 1
        n = n >> 1
    return 1 << i


def find_msb2(n):
    return 1 << (len(bin(n)[2:]) - 1)


if __name__ == '__main__':
    arr = [10, 15, 18, 7]
    for ele in arr:
        print(bin(ele), find_msb(ele))
        print(bin(ele), find_msb2(ele))
