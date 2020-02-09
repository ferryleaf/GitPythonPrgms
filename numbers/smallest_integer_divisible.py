'''
Given a positive integer K,
a. you need to find the smallest positive integer N such that
        N is divisible by K,
        and N only contains the digit 1.

b. Return the length of N.

If there is no such N, return -1.


Example 1:

Input: 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.
Example 2:

Input: 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.
Example 3:

Input: 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.


Note:

1 <= K <= 10^5

'''

class Solution():
    #11.139s: String based approach
    def smallestRepunitDivByK_1(self, K: int) -> int:
        if(K%5==0 or K%2==0):
            print('There is no such positive integer N divisible by',K)
            return -1
        else :
            if (K>=1 and K<=100000):
                    str_num=""
                    for i in range(0,K):
                        str_num = str_num + "1"
                        if (int(str_num)%K==0):
                            print("The smallest answer is N =",str_num,' which has length',i+1)
                            return i+1

        print('There is no such positive integer N divisible by',K)
        return -1

#0.289s : Mathematical formualtion
    def smallestRepunitDivByK(self, K: int) -> int:
        if((K%10) not in {1,3,5,7,9}):
            print('There is no such positive integer N divisible by',K)
            return -1
        else :
            if (K>=1 and K<=100000):
                num=1
                for i in range(1,K+1):
                    if (num%K==0):
                        print("The smallest answer is N =",num,' which has length',i)
                        return i
                    num = (num*10)+1

        print('There is no such positive integer N divisible by',K)
        return -1



def main():
    sol = Solution()
    print('*'*100)
    print(19,sol.smallestRepunitDivByK(19))
    print('*'*100)
    print(4,sol.smallestRepunitDivByK(4))
    print('*'*100)
    print(3,sol.smallestRepunitDivByK(3))
    print('*'*100)
    print(11,sol.smallestRepunitDivByK(11))
    print('*'*100)
    print(15,sol.smallestRepunitDivByK(15))
    print('*'*100)
    print(19645,sol.smallestRepunitDivByK(19645))
    print('*'*100)
    print(99999,sol.smallestRepunitDivByK(99999))
    print('*'*100)
    print(1,sol.smallestRepunitDivByK(1))
    print('*'*100)


if __name__=='__main__':
    main()
