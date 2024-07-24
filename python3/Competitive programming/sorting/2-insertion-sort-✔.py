#Ashish Singh
# ✔


class Solution:
    def insertionSort(self, alist, n):
        for i in range(0,n):                        # i = 0 to n-1
            j = i                                   # j = i 
            while (j and arr[j-1]>arr[j]):          # while and everything within j, arr[j-1]
                arr[j],arr[j-1]=arr[j-1],arr[j]
                j-=1
        return arr


if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
