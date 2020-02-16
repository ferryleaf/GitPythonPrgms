'''
You are given two strings S1 and S2. You need to find weights of both strings and compare them. The weight of a string can be obtained by adding individual weights of the characters that make the string. The weight of individual characters are the position on which they occur in the english alphabets table; for eg, a has weight 1, z has weight 26.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test cases follow. Each testcase has 2 lines
The first string S1
The second string S2

Output:
Print 1 if the weight of the first string is greater. Print 2 if the weight of the second string is greater. Print equal if the the weights are equal.

Constraints:
1<=T<=100
1<=|S1|<=1000
1<=|S2|<=1000

Example:

Input:
4
batman
superman
kira
l
goku
broly
manbat
batman

Output:
2
1
2
equal

Note: The strings contains only lowercase characters.
'''

from typing import List
import math

class Solution:
    global char_map
    char_map={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,\
        'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20, \
        'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

    def findWeights(self, str_list: List[str]) -> None:
        idx=0
        while (idx<len(str_list)):
            sum_str_1=0
            sum_str_2=0
            for val in str_list[idx]:
                sum_str_1=sum_str_1+char_map.get(val)
            for val in str_list[idx+1]:
                sum_str_2=sum_str_2+char_map.get(val)

            if (sum_str_1>sum_str_2):
                print(sum_str_1,sum_str_2,1)
            elif (sum_str_1<sum_str_2):
                print(sum_str_1,sum_str_2,2)
            else:
                print(sum_str_1,sum_str_2,'equal')
            idx=idx+2




if __name__=='__main__':
    T=int(input())
    str_list=list()
    if(T>0 and T<=100):
        for i in range(0,T*2):
            str_list.append(str(input().strip()).lower())

        sol=Solution().findWeights(str_list)
