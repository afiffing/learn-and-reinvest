#Author: Ashish Singh



class Solution:
    def bubbleSort(self,arr,n):
        for i in range(n,0,-1):        # i is n-1 to 0
            didSwap = 0
            for j in range(0,i):       # everything is inside j block, arr[j],arr[j+1]
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    didSwap = 1
            if didSwap == 0:           #is
                break
        return arr


if __name__ == "__main__":
    arr = [8,7,6,1,0,9,2]
    n = len(arr)
    Solution().bubbleSort(arr,n-1)
    for i in arr:
        print(i,end=" ")