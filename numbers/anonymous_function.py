'''
Display Powers of 2 Using Anonymous Function
'''

import math

if __name__=='__main__':
    num=int(input().rstrip())
    #print(int(math.pow(num,2)))
    pow=lambda x: math.pow(x,2)
    print(int(pow(num)))
    print((lambda x: math.pow(x,2))(5))
