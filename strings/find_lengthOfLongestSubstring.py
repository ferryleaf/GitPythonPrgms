'''
Microsoft
Given a string, find the length of the longest substring without
repeating characters.

class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.

print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10

Can you find a solution in linear time?

'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        char_map={}
        max_length = length = 0
        for index in range(0,len(s)):
            char = s[index]
            if (char_map.get(char)==None):
                char_map[char]=1
                length += 1
            else:
                if(max_length<length):
                    max_length = length
                length = 1
                char_map.clear()
                char_map[char]=1
            #print(max_length,length,char_map)
            index+=1
        if(max_length<length):
            max_length = length
        print('lengthOfLongestSubstring:',max_length)


if __name__=='__main__':
    sol = Solution()
    sol.lengthOfLongestSubstring('abrkaabcdefghijjxxx') #10
    sol.lengthOfLongestSubstring('abrkaabcdefghijjxxxabcdefghijklmnabcdef') #15
    sol.lengthOfLongestSubstring('abcdefghijklmnabcdefghijklmno')   #15
    sol.lengthOfLongestSubstring('abcdefghijklmnabcdefghijklmn')    #14
    sol.lengthOfLongestSubstring('abcdefghijklmnaabcdefghijklmn')   #14
