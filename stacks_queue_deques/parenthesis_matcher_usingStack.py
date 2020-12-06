'''
Parenthesis Matcher
'''

class Solution:
    def __init__(self):
        self.stack=[]

    def push(self,char):
        self.stack.append(char)

    def pop(self):
        return self.stack.pop()

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return (len(self.stack)==0)

    def is_balanced(self,s):
        parenthesis_map={ '[':']', '{':'}', '(':')' }
        for index in range(0,len(s)):
            if (parenthesis_map.get(s[index])):
                self.push(s[index])
            else:
                if(parenthesis_map.get(self.top())==s[index]):
                    self.pop()

        if self.is_empty():
            return True
        else:
            return False

if __name__=='__main__':
    #sol = Solution()
    #print(sol.is_balanced(input()))
    #print(sol.is_balanced(''))
    print(Solution().is_balanced('{[()]}')) # True
    print(Solution().is_balanced('{[(])}')) # False
    print(Solution().is_balanced('{{[[(())]]}}'))   # True
