'''
Digits In Factorial
Easy Accuracy: 48.64% Submissions: 35323 Points: 2
Given an integer N. Find the number of digits that appear in its factorial.
Factorial is defined as, factorial(n) = 1*2*3*4……..*N and factorial(0) = 1.


Example 1:

Input: N = 5
Output: 3
Explanation: Factorial of 5 is 120.
Number of digits in 120 is 3 (1, 2, and 0)


Example 2:

Input: N = 120
Output: 199
Explanation: The number of digits in
120! is 199

Your Task:
You don't need to read input or print anything.
Your task is to complete the function digitsInFactorial() that takes N as input
parameter and returns number of digits in factorial of N.


Expected Time Complexity : O(N)
Expected Auxilliary Space : O(1)


Constraints:
1 ≤ N ≤ 104


Solutions:
log(a*b) = log(a) + log(b)

Therefore
log( n! ) = log(1*2*3....... * n)
          = log(1) + log(2) + ........ +log(n)

Now, observe that the floor value of log base
10 increased by 1, of any number, gives the
number of digits present in that number.

Hence, output would be : floor(log(n!)) + 1.

'''

import math


def findDigits(n):
    # factorial exists only for n>=0
    if (n < 0):
        return 0

    # base case
    if (n <= 1):
        return 1

    # else iterate through n and
    # calculate the value
    digits = 0
    for i in range(2, n + 1):
        digits += math.log10(i)

    return math.floor(digits) + 1


if __name__ == '__main__':
    # Driver code
    print(findDigits(1))
    print(findDigits(5))
    print(findDigits(10))
    print(findDigits(120))
