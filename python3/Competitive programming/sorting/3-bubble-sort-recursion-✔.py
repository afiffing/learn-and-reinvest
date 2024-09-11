#Author: Ashish Singh



class Solution:
    def bubbleSort(self,arr,n):
        if n == 2:                   #iblock removed via n=1, range(n-1,0,-1)
            return
        didSwap = 0                  
        for j in range(n-1):       #no iblock, hence max of i, i.e. i=n-1 instead of range(0,i)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didSwap = 1
        if didSwap == 0:
            return
        self.bubbleSort(arr,n-1)      # equivalent of i n-1 to 0        


if __name__ == "__main__":
    arr = [8,7,6,1,0,9,2]
    Solution().bubbleSort(arr,len(arr))
    for i in arr:
        print(i,end=" ")