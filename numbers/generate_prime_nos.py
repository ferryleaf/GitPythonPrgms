'''
How to generating prime numbers upto a given number N.

Approach
Sieve of Eratosthenes

Using Sieve of Eratosthenes is the most efficient way of generating prime
numbers upto a given number N.

Following is the algorithm to find all the prime numbers less than or equal to
a given integer n by Eratosthenes' method:
    Create a list of consecutive integers from 2 to n: (2, 3, 4, ..., n).

    Initially, let p equal 2, the first prime number.

    Starting from p2, count up in increments of p and mark each of these
    numbers greater than or equal to p2 itself in the list.
    These numbers will be p(p+1), p(p+2), p(p+3), etc..

    Find the first number greater than p in the list that is not marked.
    If there was no such number, stop. Otherwise, let p now equal this number
    (which is the next prime), and repeat from step 3.

'''


def generate_prime_nos(num):
    step = 0
    arr = [x for x in range(2, num+1)]
    for ele in arr:
        if(ele*ele <= num+1):
            for val in range(ele*ele, num+1, ele):
                step += 1
                if(val in arr):
                    arr.remove(val)
    print("No. of Steps:", step)
    return arr


if __name__ == '__main__':
    num = int(input().rstrip())
    print("Prime Nos.", generate_prime_nos(num))
