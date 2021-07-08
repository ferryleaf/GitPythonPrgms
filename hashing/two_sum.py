

def keypair(A, N, X):
    # code here
    mp = dict()
    for ele in A:
        if mp.get(ele):
            mp[ele] = mp.get(ele) + 1
        else:
            mp[ele] = 1

    for ele in A:
        if (X - ele) == ele:
            if mp.get(X - ele) > 1:
                print(X, ele, X - ele)
                return 1
        else:
            if mp.get(X - ele):
                print(X, ele, X - ele)
                return 1
    return 0


if __name__ == '__main__':
    A = [335, 501, 170, 725, 479, 359, 963, 465, 706, 146, 282, 828, 962, 492,
    996, 943, 828, 437, 392, 605, 903, 154, 293, 383, 422, 717, 719, 896, 448,
    727, 772, 539, 870, 913, 668, 300, 36, 895, 704, 812, 323, 334]

    print(keypair(A, 42, 468))

    A = [1, 4, 45, 6, 10, 8]
    print(keypair(A, 6, 16))

    # important use case 1
    A = [1, 2, 5, 6, 7]
    print(keypair(A, 5, 4))

    # important use case 2
    A = [1, 2, 2, 6, 7]
    print(keypair(A, 5, 4))
