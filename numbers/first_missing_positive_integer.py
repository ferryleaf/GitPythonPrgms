'''
Stripe

Given an array of integers, find the first missing positive integer in
linear time and constant space. In other words, find the lowest positive
integer that does not exist in the array. The array can contain duplicates
and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0]
should give 3.

Use Case:
1. [3, 4, -1, 1] : 2
2. [1, 2, 0] : 3
3. [3, 4, -1, 4, 1] : 2
4. [2, 3, 4, -1, 4, 1] : 5
5. [1, 4, 3, 4] : 2
6. [1, 2, 3, 4, 8, 9] : 5
7. [2, 4, 5, -1, 1] : 3
8. [2, 3, 4, 0, 4, 5] : 1
'''

class Solution:
    def first_missing_positive_number(self,list):
        smallest = 1
        for index in range(0,len(list)):
            if(list[index]>0):
                if (smallest>=list[index]):
                    smallest+=1

    def first_missing_positive_number_sol1(self,list):
        maps={}
        for index in range(0,len(list)):
            if(list[index]>0):
                maps[list[index]] = list[index]

        for index in range(0,len(list)):
            if(list[index]>0):
                if(maps.get(index+1) == None):
                    print("Missing:",index+1)
                    break


if __name__=='__main__':
    sol = Solution()
    #sol.first_missing_positive_number()

    sol.first_missing_positive_number_sol1([3, 4, -1, 1])
    sol.first_missing_positive_number_sol1([1, 2, 0])
    sol.first_missing_positive_number_sol1([3, 4, -1, 4, 1])
    sol.first_missing_positive_number_sol1([2, 3, 4, -1, 4, 1])
    sol.first_missing_positive_number_sol1([1, 4, 3, 4])
    sol.first_missing_positive_number_sol1([1, 2, 3, 4, 8, 9])
    sol.first_missing_positive_number_sol1([2, 4, 5, -1, 1])
