#Author: Ashish Singh
# ✔


class Solution: 
    def selectionSort(self, arr,n):
        for i in range(0,n):                       # i = 0 to n-1
            mini = i  
            for j in range(i+1,n):                # j = i+1, n-1+1
                if arr[j] < arr[mini]:
                    mini = j                       #find the minimum for i loop run and swap and loop on i O(N*N)
            arr[i], arr[mini] = arr[mini], arr[i]
        
        return arr


if __name__ == "__main__":
    arr = [8,7,6,1,0,9,2]
    n = len(arr)
    Solution().quickSort(arr,0,n-1)
    for i in arr:
        print(i,end=" ")