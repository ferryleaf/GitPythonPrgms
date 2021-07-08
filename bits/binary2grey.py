

def binaryToGray(n):
    return n ^ (n >> 1)


def binaryToGray2(n):
    n_bin = bin(n)[2:]
    n_gray = n_bin[0]
    for i in range(1, len(n_bin)):
        n_gray += str(int(n_bin[i-1]) ^ int(n_bin[i]))
    return int(n_gray, 2)


if __name__ == '__main__':
    print(binaryToGray(7))
    print(binaryToGray(13))
