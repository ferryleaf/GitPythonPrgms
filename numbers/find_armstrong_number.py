'''
Find all Armstrong numbers between two integers.
Example:
num=153
len(num)=3

1^3+5^3+3^3=153

Yes Armstrong number.

'''

def find_armstrong_number(lower,upper):
    for i in range(lower,upper+1):
        order=len(str(i))
        temp=i
        sum=0
        while(temp!=0):
            digit=temp%10
            sum=sum + (digit ** order)
            temp=temp//10

        if(i==sum):
            print(i,'YES')
        #else:
        #    print(i,'NO')

if __name__=='__main__':
    lst=input().rstrip().split()
    lower=int(lst[0])
    upper=int(lst[1])
    find_armstrong_number(lower,upper)
