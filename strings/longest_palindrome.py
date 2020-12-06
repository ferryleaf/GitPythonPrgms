'''
Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.


TestCase:
"abccccdd"      #   dccaccd
"abcdcdcc"      #   dccaccd
"a"
"bb"
"ccc"
"cccc"
"-cccc"
"cccddd"  6chars      #   dcdcd dcdcd 5chars
"cccdddeee"   3c3d3e= 9chars   #   edcdcde     cedddec = 7chars
"cccccccccdddddeeeeeee" 9c5d7e =21chars         # cccceeeddcddeeecccc = 19chars
"cccccccccdddddeeeeee" 9c5d6e   =20chars        # ccccddeeeceeeddcccc = 19chars
"abcde"
"bananas" a3 b1 n2 s1=7chars       naaan=5chars
Expected Output:
7
7
1
2
3
4
4
5
7
0
19
5
'''


class Solution:
    def longestPalindrome(self, s:str)->int:
        if(len(s)>0 and len(s)<=1010):
            char_count_map={}
            flag=0
            for ele in s:
                if ((ord(ele)>=65 and ord(ele)<=90) or (ord(ele)>=97 and ord(ele)<=122)):
                    if(ele not in char_count_map):
                        char_count_map[ele]=1
                    else:
                        char_count_map[ele]=char_count_map.get(ele)+1

            sum=0
            max=0
            for key,val in char_count_map.items():
                if max<val:
                    max=val
                if val==1:
                    flag=1
                if val%2==0:
                    sum+=val
                else:
                    sum+=val-1

            if (flag==1 and sum!=0):
                sum+=1
            if (flag==1 and len(char_count_map)==1):
                return 1
            if (max%2!=0 and flag!=1):
                sum+=1

            return sum


    def longestPalindrome_2(self, s:str)->int:
        if(len(s)>0 and len(s)<=1010):
            char_count_map={}
            flag=0
            for ele in s:
                if ((ord(ele)>=65 and ord(ele)<=90) or (ord(ele)>=97 and ord(ele)<=122)):
                    if(ele not in char_count_map):
                        char_count_map[ele]=1
                    else:
                        char_count_map[ele]=char_count_map.get(ele)+1

            sum=0
            for key,val in char_count_map.items():
                if val==1:
                    flag=1
                if val%2==0:
                    sum+=val

            if (flag==1 and sum!=0):
                sum+=1
            if (flag==1 and len(char_count_map)==1):
                return 1

            return sum

if __name__=='__main__':
    s=str(input().rstrip())
    sol=Solution()
    print(sol.longestPalindrome(s))
