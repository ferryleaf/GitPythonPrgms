## Need to revisit AGAIN

def binaryToGray(n):
    return n ^ (n >> 1)


def grayToBinary(n):
    if n == 0:
        return 0
    n_bin = bin(n)[2:]
    n_gry = n_bin[0]
    for i in range(1, len(n_bin)):
        if n_bin[i] == '0':
            n_gry += n_bin[i-1]
        else:
            if n_bin[i-1] == '0':
                n_gry += '1'
            else:
                n_gry += '0'
        print(i, n_bin, n_gry[i-1], n_gry)
    return int(n_gry, 2)


if __name__ == '__main__':
    arr = [15, 4, 7, 0, 13]
    # grayToBinary: [10, 7, 5, 0, 9]
    # binaryToGray: [8, 6, 4, 0, 11]
    for ele in arr:
        print(ele, binaryToGray(ele), grayToBinary(ele))
