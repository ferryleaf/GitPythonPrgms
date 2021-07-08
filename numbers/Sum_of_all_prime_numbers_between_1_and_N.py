'''
Given a positive integer N, find the sum of all prime numbers
between 1 and N(inclusive).

Example 1:

Input: N = 5
Output: 10
Explanation: 2, 3, and 5 are prime
numbers between 1 and 5(inclusive).
Example 2:

Input: N = 10
Output: 17
Explanation: 2, 3, 5 and 7 are prime
numbers between 1 and 10(inclusive).

Input: N = 4
Output: 5
Explanation: 2, 3 are prime
numbers between 1 and 4(inclusive).

Your Task:
You don't need to read or print anyhting. Your task is to complete the function
prime_Sum() which takes N as input parameter and returns the sum of all primes
between 1 and N(inclusive).

Expected Time Complexity: O(N*log(N))
Expected Space Complexity: O(N)

Constraints:
1 <= N <= 1000000

'''


def prime_Sum(n):
    p = 2
    mp = {x: x for x in range(2, n+1)}
    while(p**2 <= n):
        for i in range(p**2, n+1, p):
            if mp.get(i):
                mp.pop(i)
        p += 1
    sum = 0
    for ele in mp:
        sum += ele
    return sum


if __name__ == '__main__':
    print(prime_Sum(5))
    print(prime_Sum(10))
    print(prime_Sum(4))
    print(prime_Sum(25))
