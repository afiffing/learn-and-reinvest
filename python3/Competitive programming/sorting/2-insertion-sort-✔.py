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
if __name__ == "__main__":
    arr = [8,7,6,1,0,9,2]
    n = len(arr)
    Solution().quickSort(arr,0,n-1)
    for i in arr:
        print(i,end=" ")
