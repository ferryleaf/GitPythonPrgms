def Solution(element):
    length = len(element)
    mid_idx = int(length/2)
    f_str= element[:mid_idx]
    s_str=""

    # To Handle String with odd length
    if(length%2!=0):
        mid_idx = mid_idx+1

    for i in range(mid_idx,length):
        s_str= element[i] + s_str

    if(f_str==s_str):
        print("Yes a Palindrome")
    else:
        print("Not a Palindrome")


if __name__=='__main__':
    element = input().strip()
    if(len(element)!=0):
        Solution(element)
