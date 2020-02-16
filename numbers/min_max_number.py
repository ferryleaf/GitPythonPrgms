'''
Finding the highest and smallest numbers along with their indices
'''

def Solution(array):
    index=min_idx=max_idx=-1
    for num in array:
        if(index==-1):
            max=min=num
        index=index+1
        if (num>=max):
            max=num
            max_idx=index+1
        if(num<=min):
            min=num
            min_idx=index+1

    print("Smallest Number:",min,' at index no. ',min_idx)
    print("Highest Number:",max,' at index no. ',max_idx)

def Solution_2(array):
    min=max=array[0]
    min_idx=max_idx=0
    for index in range(1,len(array)):
        if(min>=array[index]):
            min=array[index]
            min_idx=index
        if(max<array[index]):
            max=array[index]
            max_idx=index

    print("Smallest Number:",min,' at index no. ',min_idx+1)
    print("Highest Number:",max,' at index no. ',max_idx+1)

if __name__ =='__main__':
    n=int(input())
    if(n<=5):
        arr=list(map(int, input().rstrip().split()))
        Solution_2(arr)
