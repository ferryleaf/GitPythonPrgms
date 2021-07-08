'''
Swap all odd and even bits
Given an unsigned integer N. The task is to swap all odd bits with even bits.
For example, if the given number is 23 (00010111), it should be converted to
43(00101011). Here, every even position bit is swapped with adjacent bit on
the right side(even position bits are highlighted in the binary representation
of 23) and every odd position bit is swapped with an adjacent on the left side.

Example 1:

Input: N = 23
Output: 43
Explanation:
Binary representation of the given number
is 00010111 after swapping
00101011 = 43 in decimal.
Example 2:

Input: N = 2
Output: 1
Explanation:
Binary representation of the given number
is 10 after swapping 01 = 1 in decimal.

Your Task: Your task is to complete the function swapBits() which takes an
integer and returns an integer with all the odd and even bits swapped.


Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 109

Solution:
If the given number is 23 (00010111), it should be converted to 43 (00101011)

We can observe that we basically need to right shift (>>) all even bits
(In the above example, even bits of 23 are highlighted) by 1 so that they
become odd bits (highlighted in 43), and left shift (<<) all odd bits by 1 so
that they become even bits. The following solution is based on this
observation. The solution assumes that input number is stored using 32 bits.

Let the input number be x
1) Get all even bits of x by doing bitwise and of x with 0xAAAAAAAA.
The number 0xAAAAAAAA is a 32 bit number with all even bits set as 1 and
all odd bits as 0.
2) Get all odd bits of x by doing bitwise and of x with 0x55555555.
The number 0x55555555 is a 32 bit number with all odd bits set as 1 and
all even bits as 0.
3) Right shift all even bits.
4) Left shift all odd bits.
5) Combine new even and odd bits and return.


'''


def swapBits(n):
    # assumption: 32 bits A: 1010(4 bits) and 5: 101(3 bits)
    # even_bits = int(0xAAAAAAAA)
    # odd_bits = int(0x55555555)
    even_bits = int('1010' * 8, 2)
    odd_bits = int('0101' * 8, 2)
    evens = even_bits & n
    odd = odd_bits & n
    evens = evens >> 1
    odd = odd << 1
    return((evens | odd))


if __name__ == '__main__':
    print(swapBits(23))
