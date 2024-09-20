#solution works on local not on leetcode

class Solution():
    def __init__(self):
        self.sumStack = []

    def maximumSubarraySum(self,nums,arrLength):
        while len(nums):
            if len(nums)<arrLength:
                if self.sumStack:
                    return max(self.sumStack)
                else:
                    return 0
            else:
                unique = set()
                for i in range(arrLength):
                    unique.add(nums[i])
                if len(unique) == arrLength:
                    self.sumStack.append(sum(unique))
                nums.pop(0)
                print(nums, self.sumStack)
                

if __name__ == "__main__":
    sol = Solution()
    #nums = [4,4,4,4,4,4]
    nums = [1,1,1,1,1,1]
    #nums = [5,6,6,8,9.0,11]
    ans = sol.maximumSubarraySum(nums,3)
    print(ans)
