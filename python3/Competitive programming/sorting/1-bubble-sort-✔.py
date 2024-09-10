#Author: Ashish Singh



class Solution:
    def bubbleSort(self,arr,n):
        for i in range(n,0,-1):        # i is n-1 to 1
            didSwap = 0
            for j in range(0,i):       # everything is inside j block, arr[j],arr[j+1], "j block is bubble"
                if arr[j]>arr[j+1]:     # j is first, j+1 is next, swap when first > next, right to left traverse
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    didSwap = 1
            if didSwap == 0:           # no more swap, no more bubble
                break
        return arr


if __name__ == "__main__":
    arr = [8,7,6,1,0,9,2]
    Solution().bubbleSort(arr,len(arr)-1)
    for i in arr:
        print(i,end=" ")


#################################################################################################################################        

# # Please check the bubble sort example

# arr = [8,7,6,1,0,9,2]
#           0,1,2,3,4,5,6  
# i=6,didSwap=0
# j= 0 to 6
# didSwap=1

# i=6,j=0,8>7,8,7=7,8

# arr = [7,8,6,1,0,9,2]

# i=6,j=8,8>6,8,6=6,8

# arr = [7,6,8,1,0,9,2]

# i=6,j=8,8>1,8,1=1,8

# arr = [7,6,1,8,0,9,2]

# i=6,j=8,8>0,8,0=0,8

# arr = [7,6,1,0,8,9,2]

# i=6,j=8,8>9,8,9=9,8

# arr = [7,6,1,0,8,9,2]
# i=6,j=9,9>2,9,2=2,9

# arr = [7,6,1,0,8,2,9]

# i=5,j=0 to 5

# i=5,j=7,7>6,7,6=6,7

# arr = [6,7,1,0,8,2,9] ->  arr = [6,1,7,0,8,2,9] ->  arr = [6,1,0,7,8,2,9] ->  arr = [6,1,0,7,8,2,9] -> arr = [6,1,0,7,2,8,9]

# i=4,j=0 to 4

# # arr = [6,1,0,7,2,8,9] -> [1,6,0,7,2,8,9] -> [1,0,6,7,2,8,9] -> [1,0,6,7,2,8,9] -> [1,0,6,2,7,8,9] 

# i=3,j=0 to 3

# # arr = [1,0,6,2,7,8,9] -> [0,1,6,2,7,8,9] -> [0,1,6,2,7,8,9] -> [0,1,2,6,7,8,9]

# didSwap = 0
