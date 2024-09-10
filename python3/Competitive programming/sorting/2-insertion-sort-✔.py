#Ashish Singh
# ✔


class Solution:
    def insertionSort(self, arr, n):
        for i in range(n):                          # i = 0 to n-1
            j = i                                   # j = i 
            while (j>0 and arr[j-1] > arr[j]):      # while and everything within j, arr[j-1]
                arr[j],arr[j-1]=arr[j-1],arr[j]
                j-=1


if __name__ == "__main__":
    arr = [8,7,6,1,0,9,2]
    Solution().insertionSort(arr,len(arr))
    for i in arr:
        print(i,end=" ")


#################################################################################################################################        

# # Please check the insertion sort example

# arr = [8,7,6,1,0,9,2]

# i= 0 to 6

# j=0, j<0

# i=1, j=1, 8>7, arr = [7,8,6,1,0,9,2]
# j=0

# i=2, j=2, arr[1]>arr[2], 8>6, arr = [7,6,8,1,0,9,2]
    # i=2, j=1, arr[0]>arr[1], 8>6, arr = [6,7,8,1,0,9,2]

# i=3, ....

