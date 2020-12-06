'''
Uber

Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except
the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1],
the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?



Use Case:
1: [1, 2, 3, 4, 5] = [120, 60, 40, 30, 24].
2: [3, 2, 1] = [2, 3, 6].
3: [0, 2, 3, 4] = [24, 0, 0, 0]
'''

class Solution:
    def productArray(self,list):
        contains_zero=0
        prd=1
        for ele in list:
            ele = int(ele)
            if(ele == 0):
                contains_zero=1
            else:
                prd*=ele

        new_list=[]
        for index in range(0,len(list)):
            if(list[index]!=0):
                if(contains_zero):
                    new_list.append(int(0))
                else:
                    new_list.append(prd/list[index])
            else:
                if(list[index]==0):
                    new_list.append(prd)

        print('old',list)
        print('new',new_list)

    def productArray_sol2(self,list):
        new_list=[]
        contains_zero=0
        if (0 in list):
            contains_zero=1

        for i in range(0,len(list)):
            prd=1
            for j in range(0,len(list)):
                if(i!=j):
                    if(contains_zero):
                        prd*=0
                    else:
                        prd*=list[j]
            new_list.append(prd)



if __name__=='__main__':
    sol = Solution()
    sol.productArray([1, 2, 3, 4, 5])
    sol.productArray([3, 2, 1])
    sol.productArray([0, 2, 3, 4])
    sol.productArray([4, 0, 2, 3, 4])

    sol.productArray_sol2([1, 2, 3, 4, 5])
    sol.productArray_sol2([3, 2, 1])
    sol.productArray_sol2([0, 2, 3, 4])
    sol.productArray_sol2([4, 0, 2, 3, 4])
