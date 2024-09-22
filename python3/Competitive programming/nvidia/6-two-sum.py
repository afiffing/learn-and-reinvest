
class Solution():

    def __init__(self):
        self.arr = []

    def twoSum(self,nums,target):
        for i in range(len(nums)):
            dupNums = nums.copy()
            dupNums.remove(dupNums[i])
            if (target - nums[i]) in dupNums:   
                self.arr.append(i)
        return self.arr




if __name__ == "__main__":
    s1 = Solution()
    
    #print(s1.twoSum([2,7,11,15],9))
    #print(s1.twoSum([3,2,4],6))
    print(s1.twoSum([3,3],6))
