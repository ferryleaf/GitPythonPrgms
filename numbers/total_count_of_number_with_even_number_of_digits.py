class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        if (len(nums)>=1 and len(nums)<=500):
            for num in nums:
                if (num>=1 and num<=int(math.pow(10,5))) :
                    leng = len(str(num))
                    if (leng>=1 and leng<=500 and leng%2==0):
                        count=count + 1

        return count

def main():
    sol = Solution()
    print(sol.findNumbers([555,901,482,1771]))
    print(sol.findNumbers([12,345,2,6,7896]))


if __name__ == '__main__':
    main()
