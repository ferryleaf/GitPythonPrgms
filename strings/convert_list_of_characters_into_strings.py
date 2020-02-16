'''
Given a list of characters, merge all of them into a string.

Input:
First line of the input contains an integer T, denoting the number of testcases. Then T test case follows. Each testcase contains two lines:-
The number of characters in the array N.
The array of characters separated by space

Output:
For each testcase, print the character array converted into a string.

Constraints:
1<=T<=100
10<=N<=100


Example:

Input:
2
13
g e e k s f o r g e e k s
11
p r o g r a m m i n g

Output:
geeksforgeeks
programming
'''


if __name__=='__main__':
    T=int(input())
    str_list=list()
    if(T>0 and T<=100):
        for i in range(0,T*2):
            str_list.append(str(input().rstrip()).lower())

    for i in range(0,len(str_list)):
        if(i%2!=0):
            str_arry=''
            for ele in str_list[i]:
                if (ele!=' '):
                    str_arry=str_arry+ele
            print(str_arry)
