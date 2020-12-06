

def reverse_array(arr):
    # return arr[::-1]
    return arr.reverse()


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = list(map(int, input().rstrip().split()))
        for ele in arr[::-1]:
            print(ele, end=" ")
        print()
