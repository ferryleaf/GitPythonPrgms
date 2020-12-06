'''
Balanced Bracket using List DS.
'''

class Solution():
    def is_balanced(self,s):
        stack=[]
        parenthesis_map={ '[':']', '{':'}', '(':')' }
        for index in range(0,len(s)):
            if (parenthesis_map.get(s[index])):
                stack.append(s[index])
            else:
                if(parenthesis_map.get(stack[-1])==s[index]):
                    stack.pop()
        if (len(stack)==0):
            return True
        else:
            return False

if __name__=='__main__':
    #print(Solution().is_balanced())
    print(Solution().is_balanced('{[()]}')) # True
    print(Solution().is_balanced('{[(])}')) # False
    print(Solution().is_balanced('{{[[(())]]}}'))   # True
