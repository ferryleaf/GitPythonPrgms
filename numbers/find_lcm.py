'''
The least common multiple (L.C.M.) of two numbers is the smallest positive integer
that is perfectly divisible by the two given numbers.

For example, the L.C.M. of 12 and 14 is 84.
'''

#Number1 * Number2 = L.C.M. * G.C.D.
def find_gcd(num1:int, num2:int)->int:
    while num2:
        num1,num2=num2,num1%num2
    return num1

def find_lcm(num1:int, num2:int)->int:
    return (num1*num2)//find_gcd(num1,num2)

if __name__=='__main__':
    lst=input().rstrip().split()
    print(find_lcm(int(lst[0]),int(lst[1])))
