'''
First and Last Indices of an Element in a Sorted Array.
AirBNB:

Given a sorted array, A, with possibly duplicated elements.
Find the indices of the first and last occurrences of a target element, x.
Return -1 if the target is not found.

Example:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
Here is a function signature example:

class Solution:
  def getRange(self, arr, target):
    # Fill this in.

# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

'''

class Solution:
  def getRange(self, arr, target):
      start = end = -1
      index=0
      for ele in arr:
          ele = int(ele)
          if (ele == target and start == -1):
              start = index
          if (arr[index-1] == target and arr[index] != target):
              end = index-1
          index+=1
      print(start,end)


  def getRange_sol1(self, arr, target):
      start = end = -1
      for index in range(0,len(arr)-1):
          if (arr[index]==target and start==-1):
              start = index
          if (arr[index]!=target and arr[index+1]==target):
              start = index + 1
          elif (arr[index]==target and arr[index+1]!=target):
              end = index
          index+=1
      print(start,end)



if __name__=='__main__':
    sol = Solution()
    #arr = input().split()
    #x = int(input())
    #sol.getRange(arr,x)
    sol.getRange([1,3,3,5,7,8,9,9,9,15],9) # 6,8
    sol.getRange([1, 2, 2, 2, 2, 3, 4, 7, 8, 8],9) # -1,-1
    sol.getRange([100, 150, 150, 153],150) # 1,2
    sol.getRange([1,2,3,4,5,6,10],9)    # -1,-1
    print('*' * 50)
    sol.getRange_sol1([1,3,3,5,7,8,9,9,9,15],9) # 6,8
    sol.getRange_sol1([1, 2, 2, 2, 2, 3, 4, 7, 8, 8],9) # -1,-1
    sol.getRange_sol1([100, 150, 150, 153],150) # 1,2
    sol.getRange_sol1([1,2,3,4,5,6,10],9)    # -1,-1
