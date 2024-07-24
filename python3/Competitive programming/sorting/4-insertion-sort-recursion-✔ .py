#Ashish Singh
# ✔


class Solution:
    def insertionSort(self, alist, i, n):
        if i == n:
            return
        j = i
        while (j and arr[j] < arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        
        self.insertionSort(arr,i+1,n)
        


if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,0,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
