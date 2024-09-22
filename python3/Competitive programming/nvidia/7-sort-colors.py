
class Solution():

    def sortColors(self,nums,n):

        for i in range(n-1,0,-1):
            didSwap = 0
            for j in range(i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    didSwap = 1
            if didSwap == 0:
                break
        return nums


if __name__ == "__main__":
    s1 = Solution()
    print(s1.sortColors([2,0,2,1,1,0],len([2,0,2,1,1,0])))