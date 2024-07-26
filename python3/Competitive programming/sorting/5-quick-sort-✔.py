#Ashish Singh
# ✔

# e.g. 8 7 6 1 0 9 2

class Solution:
    def partition(self,arr,low,high):
        
        pivot = arr[high]                      # decide pivot
        i = low - 1                            
        
        for j in range (low, high):            # 
            if arr[j]<=pivot:
                i=i+1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[high]=arr[high],arr[i+1]
        
        return i+1                            # find its rightful position to divide/split the array   # 1 0 2 8 7 9 6 
    
    def quickSort(self,arr,low,high):
        
        if low<high:
            pi = self.partition(arr,low,high) # 2
            
            self.quickSort(arr,low, pi-1)     # low to 2       
            self.quickSort(arr,pi+1, high)    # 2+1 to high
    


    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends