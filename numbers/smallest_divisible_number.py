'''
LCM of First n Natural Numbers

Given a number N, find an integer denoting the smallest number evenly divisible
by each number from 1 to n.


Example 1:

Input:
N = 3
Output: 6
Explanation: 6 is the smallest number
divisible by 1,2,3.

Example 2:

Input:
N = 6
Output: 60
Explanation: 60 is the smallest number
divisible by 1,2,3,4,5,6.

Your Task:
You dont need to read input or print anything. Complete the function
getSmallestDivNum() which takes N as input parameter and returns the smallest
number evenly divisible by each number from 1 to n.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 25
'''


def getSmallestDivNum(n):
    lcm = 1
    for ele in range(2, n+1):
        lcm = find_gcf(lcm, ele)
    return int(lcm)


def find_gcf(a, b):
    mul = a*b
    while (b != 0):
        a, b = b, a % b
    return mul/a


if __name__ == '__main__':
    print("Smallest Divisible Number:", getSmallestDivNum(int(input())))


r1, r2 = (-b + (((b**2) - (4*a*c))**0.5)) / (2*a), (-b - (((b**2) - (4*a*c))**0.5)) / (2*a)
        if b**2 >= 4*a*c:
            return int(r1),int(r2)
        else:
