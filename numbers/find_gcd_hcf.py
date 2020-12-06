'''
Find the GCD of two numbers using two different methods:
a. function + loops
b. Euclidean algorithm
'''


class Solution:
    # More Efficient than the loop style
    # #Euclidean Algorithm  : Number1 * Number2 = L.C.M. * G.C.D.
    def find_gcd_hcf_euclidean(self, num1: int, num2: int) -> int:
        while(num2):
            num1, num2 = num2, num1 % num2
        return num1

    def find_gcd_hcf_func_loops(self, num1: int, num2: int) -> int:
        if (num1 > num2):
            smallest = num2
        else:
            smallest = num1

        hcf = 1
        for i in range(1, smallest + 1):
            if((num1 % i) == 0 and (num2 % i) == 0):
                hcf = i
        return hcf


'''
Dry run for GCD
a   b   a%b
30  42  12
42  12  6
12  6   0
6   0   6
0   6

GCD=6; a*b=1260
LCM = (a*b)/GCD = 210
'''


def gcd(a, b):
    # Outside class, because you can't call recursive function inside the class
    if (a == 0):
        return b
    return gcd(b % a, a)


if __name__ == '__main__':
    lst = input().rstrip().split()
    print(Solution().find_gcd_hcf_func_loops(int(lst[0]), int(lst[1])))
    print(Solution().find_gcd_hcf_euclidean(int(lst[0]), int(lst[1])))
    print(gcd(int(lst[0]), int(lst[1])))
