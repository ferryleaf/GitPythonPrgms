'''
Given an integer n, your task is to complete the function convertToRoman which
prints the corresponding roman number of n. Various symbols and their values
are given below.

I 1
V 5
X 10
L 50
C 100
D 500
M 1000


Example 1:

Input:
n = 5
Output: V


Example 2:

Input:
n = 3
Output: III


Your Task:
Complete the function convertToRoman() which takes an integer N as input
parameter and returns the equivalent roman.


Expected Time Complexity: O(log10N)
Expected Auxiliary Space: O(log10N * 10)


Constraints:
1<=n<=3999
num = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X",
        40:"XL", 50:"L", 90:"XC",  100:"C",
        400:"CD", 500:"D", 900:"CM", 1000:"M"}

Decimal value (v)	Roman numeral (n)
	1						I
	4						IV
	5						V
	9						IX
	10						X
	40						XL
	50						L
	90						XC
	100						C
	400						CD
	500						D
	900						CM
	1000					M

'''


# 0.02
def convertRoman(n):
    roman = ""
    print(n, end=" ")
    while (n != 0):
        if n >= 1 and n < 4:
            roman += (n//1 * 'I')
            n %= 1

        if n >= 4 and n < 5:
            roman += (n//4 * 'IV')
            n %= 4

        if n >= 5 and n < 9:
            roman += (n//5 * 'V')
            n %= 5

        if n >= 9 and n < 10:
            roman += (n//9 * 'IX')
            n %= 9

        if n >= 10 and n < 40:
            roman += (n//10 * 'X')
            n %= 10

        if n >= 40 and n < 50:
            roman += (n//40 * 'XL')
            n %= 40

        if n >= 50 and n < 90:
            roman += (n//50 * 'L')
            n %= 50

        if n >= 90 and n < 100:
            roman += (n//90 * 'XC')
            n %= 90

        if n >= 100 and n < 400:
            roman += (n//100 * 'C')
            n %= 100

        if n >= 400 and n < 500:
            roman += (n//400 * 'CD')
            n %= 400

        if n >= 500 and n < 900:
            roman += (n//500 * 'D')
            n %= 500

        if n >= 900 and n < 1000:
            roman += (n//900 * 'CM')
            n %= 900

        if n >= 1000:
            roman += (n//1000 * 'M')
            n %= 1000

    return roman


def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            print(sym[i], end="")
            div -= 1
        i -= 1
    print()


def printRoman2(number):
    # Works in python 3.7, dictionary gurantees to preserve ordering of insertion.
    # Thereby, inserted in reverse order.
    # Above 2 approaches are also correct. But this looks elegant.
    # One must know, symbols for 1, 4, 5, 9, 10 likewise multiples of 10 of it.
    roman_literals = {1000: "M", 900: "CM", 500: "D", 400: "CD",
                      100: "C", 90: "XC", 50: "L", 40: "XL",
                      10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

    for num in roman_literals.keys():
        if number == 0:
            break
        else:
            div = number // num
            number %= num
            print(div * roman_literals.get(num), end="")
    print()


# 0.01
def printRoman3(number):
    # Works in python 3.5+, dictionary gurantees to preserve ordering of insertion.
    # Thereby, inserted in reverse order.
    # Above 2 approaches are also correct. But this looks elegant.
    # One must know, symbols for 1, 4, 5, 9, 10 likewise multiples of 10 of it.
    roman_literals = {1000: "M", 900: "CM", 500: "D", 400: "CD",
                      100: "C", 90: "XC", 50: "L", 40: "XL",
                      10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

    for num in sorted(roman_literals.keys(), reverse=True):
        if number == 0:
            break
        else:
            div = number // num
            number %= num
            print(div * roman_literals.get(num), end="")
    print()


def convertRoman2(n):
    roman = ''
    roman_literals = {1000: "M", 900: "CM", 500: "D", 400: "CD",
                      100: "C", 90: "XC", 50: "L", 40: "XL",
                      10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

    for num in roman_literals.keys():
        if n == 0:
            break
        else:
            div = n // num
            n %= num
            print(div, n, div * roman_literals.get(num), end="")
            roman += div * roman_literals.get(num)
    return roman


if __name__ == '__main__':
    '''
    arr = [1, 3, 4, 5, 8, 9, 10, 12, 15, 18, 19, 20, 40, 49, 50, 80, 90, 100,
           101, 120, 140, 150, 180, 190, 200, 399, 400, 450, 900, 916, 990,
           1000, 1900, 1999, 3594, 3794, 354]
    for ele in arr:
        print(convertRoman(ele))
        printRoman(ele)
        printRoman2(ele)    # Recommended
        print()
    '''
printRoman2(5)
printRoman3(5)
#print(convertRoman2(5))
