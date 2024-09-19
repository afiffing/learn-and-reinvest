class Solution():
    def __init__(self):
        self.sumStack = []

    def subArrSum(self,nums,arrLength):
        if len(nums)<arrLength:
            return 0
        else:
            for i in range(arrLength):
                elemSum += nums[i]
            self.sumStack.append(elemSum)
            nums.pop(0)
            subArrSum(self,nums,arrLength)
        return max(self.sumStack)

