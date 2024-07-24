#Author: Ashish Singh



class Solution:
    def bubbleSort(self,arr,n):
        for i in range(n,0,-1):        # i is n-1 to 0
            didSwap = 0
            for j in range(0,i):       # everything is inside j block, arr[j],arr[j+1]
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    didSwap = 1
            if didSwap == 0:         
                break
        return arr


#forget about passing the value
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().bubbleSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()