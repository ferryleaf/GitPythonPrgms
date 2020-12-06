'''
The factorial of a number is the product of all the integers from 1 to that number.

For example, the factorial of 6 is 1*2*3*4*5*6 = 720.
Factorial is not defined for negative numbers and the factorial of zero is one, 0! = 1.
'''
def find_factors_recursion(num:int) -> int:
    if (num!=0):
        return (num*find_factors_recursion(num-1))
    else:
        return 1

if __name__=='__main__':
    print(find_factors_recursion(int(input().rstrip())))
