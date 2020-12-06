''' Facebook

Given a list of numbers, where every number shows up twice except for one number,
find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1
Here's the function signature:

def singleNumber(nums):
  # Fill this in.

print singleNumber([4, 3, 2, 4, 1, 3, 2])
# 1

Challenge: Find a way to do this using O(1) memory.
'''

class Solution:
    # Extract in O(1) space complexity
    def singleNumber(self,nums):
        print(nums)
        num_map={}
        for num in nums:
            if (num_map.get(num) == None):
                num_map[num] = 1
            else:
                num_map.pop(num)
        print(num_map)

    # Extract in O(1) time complexity
    def singleNumber_sol1(self,nums):
        num_map={}
        for num in nums:
            if (num_map.get(num.strip()) == None):
                num_map[num] = 1
            else:
                num_map[num] = num_map.get(num) + 1

        new_num_map={}
        for key,val in num_map.items():
            new_num_map[val] = key

        print(new_num_map.get(1))



if __name__ =='__main__':
    nums = input().split(' ')
    sol = Solution()
    sol.singleNumber(nums)
