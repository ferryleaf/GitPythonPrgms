'''
Given an array of size N, swap the kth element from beginning with kth element from end.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains 2 lines of input:
The first line contains an integer N, where N is the size of array.
The second line contains N integers(elements of the array) sperated with spaces.

Output:
For each test case, print the modified array.

Constraints:
1 ≤ T ≤ 200
1 ≤ K ≤ N ≤ 500
1 ≤ A[i] ≤ 1000

Example:
Input
1
8 3
1 2 3 4 5 6 7 8
Output
1 2 6 4 5 3 7 8
'''

def solution(arry_lst,K):
    arry_lst_int=list()
    f_ele=arry_lst[K-1]
    l_ele=arry_lst[len(arry_lst)-K]
    temp=f_ele
    arry_lst[K-1]=l_ele
    arry_lst[len(arry_lst)-K]=temp
    for ele in arry_lst:
        arry_lst_int.append(int(ele))
    return arry_lst_int


if __name__=='__main__':
    T=int(input().rstrip())
    if(T>0 and T<=200):
        arry_sze_kth_num_lst=arry_lst=list()
        for i in range(0,T):
            arry_sze_kth_num_lst=(input().rstrip().split())
            N=int(arry_sze_kth_num_lst[0])
            K=int(arry_sze_kth_num_lst[1])
            arry_lst=input().rstrip().split()
            print(solution(arry_lst,K))
