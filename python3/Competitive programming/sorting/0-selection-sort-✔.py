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


#forget about passing the value
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()