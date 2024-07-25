#Author: Ashish Singh



class Solution:
    def bubbleSort(self,arr,n):
        if n == 1:                   #base condition added, n=1, make i=n-1=0
            return
        didSwap = 0                  #iblock removed via i=n-1
        for j in range(0,n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didSwap = 1
        if didSwap == 0:
            return
        self.bubbleSort(arr,n-1)      # equivalent of i n-1 to 0        


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