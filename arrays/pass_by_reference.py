

class Solution:
    def reverseInGroups(self, arr, N, K):
        arr[:K] = arr[K-1::-1]
        arr[K:N] = arr[N-1:K-1:-1]
        # print("Values inside the function: ", arr)
        return

    def changeme(self, mylist):
        mylist.append([1, 2, 3, 4])
        print("Values inside the function: ", mylist)
        return


if __name__ == '__main__':
    '''
    mylist = [10, 20, 30]
    print("Values before the function call: ", mylist)
    Solution().changeme(mylist)
    print("Values outside the function: ", mylist)
    '''
    print()

    arr = [5, 6, 8, 9]
    print("Values before the function call: ", arr)
    Solution().reverseInGroups(arr, 4, 3)
    print("Values outside the function: ", arr)

    print()
    # 38 22 16 30 82 0 70 55 96 48 64 93 36
    # 36 13 94 14 57 10 88 70 43 91 50 19 53
    # 67 82 18 58 54 32 59
    arr = [36, 93, 64, 48, 96, 55, 70, 0, 82, 30, 16, 22, 38,
           53, 19, 50, 91, 43, 70, 88, 10, 57, 14, 94, 13, 36,
           59, 32, 54, 58, 18, 82, 67]
    print("Values before the function call: ", arr)
    Solution().reverseInGroups(arr, 33, 13)
    print("Values outside the function: ", arr)
