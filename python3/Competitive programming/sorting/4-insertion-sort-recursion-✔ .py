#Ashish Singh
# ✔


class Solution:
    def insertionSort(self, alist, i, n):
        if i == n:
            return
        j = i
        while (j>0 and arr[j] < arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        
        self.insertionSort(arr,i+1,n)
        


if __name__ == "__main__":
    arr = [8,7,6,1,0,9,2]
    n = len(arr)
    Solution().insertionSort(arr,0,n)
    for i in arr:
        print(i,end=" ")
