'''
Given a number x, your task is to find if this number is Deficient number or not. A number x is said to be Deficient Number if sum of all the divisors of the number denoted by divisorsSum(x) is less than twice the value of the number x. And the difference between these two values is called the deficiency.

Mathematically, if below condition holds the number is said to be Deficient:
divisorsSum(x) < 2*x
deficiency = (2*x) - divisorsSum(x)


Examples:

Input: 21
Output: YES
Divisors are 1, 3, 7 and 21. Sum of divisors is 32.
This sum is less than 2*21 or 42.

Input: 12
Output: NO

Input: 17
Output: YES


Input:
The first line of input contains an integer T denoting the no of test cases.
Then T test cases follow. Each line contains an integer x.

Output:
For each test case in a new line print 1 if the no is a Deficient number else print 0.

Constraints:
1 <= T <= 10000
1 <= x <= 10000

Example:
Input:
3
21
12
17
Output:
1
0
1
'''
import math
def solution(num_lst):
    for ele in num_lst:
        sum=0
        for i in range(1,ele+1):
            if (ele%i==0):
                sum=sum+i
        if(sum<(2*ele)):
            print('YES')
        else:
            print('NO')

def solution_2(num_lst):
    for ele in num_lst:
        sum=0
        for i in range(1,int(math.sqrt(ele))+1):
            if (i==int(math.sqrt(ele)) and float(ele)%math.sqrt(ele)==0.0):
                sum=sum+i
            elif(ele%i==0):
                sum=sum+i+(ele/i)

        if(sum<(2*ele)):
            print(1)
        else:
            print(0)


if __name__=='__main__':
    T=int(input())
    num_lst=[]
    if (T>0 and T<=10000):
        for i in range(0,T):
            num_lst.append(int(input().rstrip()))

        solution_2(num_lst)
