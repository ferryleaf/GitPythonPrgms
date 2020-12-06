class Solution:
    def find_character_from_ASCIIValue(self,num:int)->str:
        return chr(num)

    def findASCIIValue(self,s:str)->int:
        return ord(s)


if __name__=='__main__':
    print(Solution().findASCIIValue(input().rstrip()))
    print(Solution().find_character_from_ASCIIValue(int(input().rstrip())))
