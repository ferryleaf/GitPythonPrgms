'''
Sorting a list with 3 unique numbers : Dutch National Flag problem
Google:

Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]
def sortNums(nums):
  # Fill this in.

print sortNums([3, 3, 2, 1, 3, 2, 1])
# [1, 1, 2, 2, 3, 3, 3]

Challenge: Try sorting the list using constant space.
Sol : Dutch National Flag problem
'''

# Below is not constant space but 2n space complexity
def sortNums_sol1(nums):
    num_map={}
    num_map[0] = num_map[1] = num_map[2] = 0
    for num in nums:
        num = int(num)
        if (num_map.get(num)== None):
            num_map[num] = 1
        else:
            num_map[num] = num_map.get(num) + 1

    nums_list = []
    for key,val in num_map.items():
        for i in range(0,val):
            nums_list.append(key)
    print(nums_list)

# 2,0,2,1,1,0
def swap(num1,num2):
    return num2,num1

'''
S1: Initialise with 3 pointers: low,mid & high | low=mid=0 and high=length of the list
S2: if list[mid] value = 0, then swap(list[low],list[mid]) & low++,mid++ increment the counter
S3: if list[mid] value = 1, then mid++ increment
S4: if list[mid] value = 2, then swap(list[mid],list[high]) & high-- decrement the counter
S5: Continue S2-S4 until mid<high
'''
# Dutch National Flag Soluton : using constant space & sort the list in O(n) time.
def sortNums_sol2(nums):
    low = mid = 0
    high = len(nums)-1
    #print(nums,low,mid,high)
    while(mid<high):
        if (nums[mid]==0):
            nums[low],nums[mid] = swap(nums[low],nums[mid])
            low+=1
            mid+=1

        if (nums[mid]==1):
            mid+=1

        if (nums[mid]==2):
            nums[mid],nums[high] = swap(nums[mid],nums[high])
            high-=1
        #print(nums,low,mid,high)
    print(nums)

if __name__=='__main__':
    #nums = input().rstrip().split()
    #sortNums(nums)
    #nums = [2,0,2,1,1,0]
    nums = [2,0,2,1,1,0,0,2,1,2,1,0,2,1]
    sortNums_sol2(nums)


# Reference URL : https://www.youtube.com/watch?v=sEQk8xgjx64
