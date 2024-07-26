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
    



if __name__ == "__main__":
    arr = [8,7,6,1,0,9,2]
    n = len(arr)
    Solution().quickSort(arr,0,n-1)
    for i in arr:
        print(i,end=" ")