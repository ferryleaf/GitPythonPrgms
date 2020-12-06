def Solution(element):
    new_num=0
    while(element!=0):
        new_num=element%10 *10 + new_num
        element=element/10

    if(new_num==element):
        print("Yes a Palindrome")
    else:
        print("Not a Palindrome")


if __name__=='__main__':
    element = int(input().strip())
    if(len(element)!=0):
        if(element>0):
            Solution(element)
        else:
            print("Not a Palindrome")
