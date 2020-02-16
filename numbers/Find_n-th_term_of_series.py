'''
Find n-th term of series 1, 3, 6, 10, 15, 21

Given a number N, find the Nth term in the series 1, 3, 6, 10, 15, 21…

Input :
The first line of input contains a positive integer T denoting the number of testcases. For each test case, there will be a single line containing an integer N.

Output:
For each testcase, print the Nth term.

Constraints:
1 <= T <= 100
1 <= N <= 1000

Examples:
Input:
2
3
4

Output:
6
10
'''
def Solution(num,max_ele):
    series_list=[]
    sum=0
    for i in range(1,max_ele+1):
        sum=sum + i
        series_list.append(sum)


    print(len(series_list))
    print(series_list)

    for idx in num:
        print(series_list[idx-1])




if __name__=='__main__':
    T=int(input())
    num=[]
    max_ele=-1
    if(T>0 and T<=100):
        for i in range(0,T):
            N= int(input())
            if(N>0 and N<=1000):
                num.append(N)
                if(max_ele<N):
                    max_ele=N
            else:
                break
        print("Max Element",max_ele)
        Solution(num,max_ele)
