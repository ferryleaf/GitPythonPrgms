


class Solution :
    def reverseVowels(self, s :str) -> str:
        new_text=''
        for ele in text:
            if ele not in ['a','e','i','o','u','A','E','I','O','U']:
                new_text=new_text+ele
        return new_text


if __name__=='__main__':
    text = str(input())
    solv = Solution()
    #solv.removeVowels(text)
    print(solv.reverseVowels(text))
