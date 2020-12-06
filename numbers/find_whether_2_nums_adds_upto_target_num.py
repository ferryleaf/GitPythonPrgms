'''
Two-Sum
FaceBook
Given a list of numbers, and a target number k.
Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5,
return true since 4 + 1 = 5.

def two_sum(list, k):
  # Fill this in.

print two_sum([4,7,1,-3,2], 5)

# True

Try to do it in a single pass of the list.
5 - [4,7,1,-3,2] = [1,-2,4,8,3]
5
4 7 1 -3 2
'''

class Solution:
    def two_sum(self, list, k):
        flag=0
        num_map={}
        for num in list:
            num = int(num)
            num_map[num] = k - int(num)
            if(num_map.get(num) in num_map.keys()):
                flag=1

        if (flag==1):
            print('True')
        else:
            print('False')


if __name__=='__main__':
    k = int(input())
    list = input().split(' ')
    sol = Solution()
    sol.two_sum(list,k)
