#code


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = list(map(int, input().rstrip().split()))
        for ele in arr[::-1]:
            print(ele, end=" ")
        print()
