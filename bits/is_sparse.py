

def isSparse(n):
    print(bin(n))
    prev = -1
    curr = -1
    while(n):
        if curr == -1 and prev == -1:
            curr = prev = (n >> 0) & 1
        else:
            prev = curr
            curr = (n >> 1) & 1

        if prev & curr == 1:
            return "Non-Sparse"
        n = n >> 1
    return "Sparse"


# 0.62 secs
def isSparse2(n):
    bin_n = bin(n)[2:]
    for i in range(len(bin_n)-1):
        if int(bin_n[i]) & int(bin_n[i+1]) == 1:
            return "Non-Sparse"
    return "Sparse"


if __name__ == '__main__':
    '''
    # 2  Sparse
    # 3  No
    # 5  Sparse
    # 6  No
    # 12 No
    # 13 No
    # 14 No
    # 10 Sparse
    '''
    arr = [2, 3, 5, 6, 12, 13, 14, 10]
    for ele in arr:
        print(ele, ":", isSparse(ele))
        print(ele, ":", isSparse2(ele))
