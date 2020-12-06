



class Solution :
    def romantoInt(self,s:str)->int:
        roman={'i':1,'v':5,'x':10,'l':50,'c':100,'d':500,'m':1000}
        if(len(s)==1):
            return(roman.get(s))

        sum=0
        for i in range(1,len(s)+1,2):
            ele_1=roman.get(s[i-1])
            if(i==len(s)):
                ele_2=0
            else:
                ele_2=roman.get(s[i])

            if(ele_1>=ele_2):
                sum=sum+ele_1+ele_2
            else:
                sum=sum+ele_1+ele_2-2
            #print(sum,ele_1,ele_2,i)
        return sum

if __name__=='__main__':
    T=str(input().strip())
    sol=Solution()
    print(sol.romantoInt(T.lower()))
#XXVII
