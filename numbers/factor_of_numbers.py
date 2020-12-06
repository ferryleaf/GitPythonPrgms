'''
Find the Factors of a Number:
Example:
The factors of 320 are:
1
2
4
5
8
10
16
20
32
40
64
80
160
320
 '''
import math

class Solution:
    def find_factors(self,num:int) -> None:
        factors=list()
        for i in range(1,int(math.sqrt(num))+1):
            if(num%i==0):
                factors.append(i)
                factors.append(int(num/i))
        print(factors)

if __name__=='__main__':
    Solution().find_factors(int(input()))
