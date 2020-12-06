'''
Find the Second Max Number from the Array
'''

class Solution:
    def solution(self,list):
        max_1 = max_2 = list[0]
        for index in range(1,len(list)):
            ele = list[index]
            if (max_1 < ele):
                max_2=max_1
                max_1=ele
            if(max_1==max_2):
                max_2=ele
            if((max_2<max_1) and (max_1>ele) and (max_2<=ele)):
                max_2=ele
        print("Max_1:",max_1,"  Max_2:",max_2)


if __name__=='__main__':
    sol = Solution()
    sol.solution([1,2,3,4,5,6,7])   #6
    sol.solution([4,2,3,5,61,8,4,1])    #8
    sol.solution([67,45,23,44,30,0,1,3,45]) #45
    sol.solution([67,45,23,44,68,0,1,3,45]) #67
    sol.solution([67,45,77,44,30,0,1,3,45]) #67
    sol.solution([87,45,77,44,30,0,1,3,45]) #77
