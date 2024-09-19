
class Solution():

    def missNum(self,nums):
        for elem in range (len(nums)+1):
            if elem not in nums:
                return elem

    def missNumMath(self,nums):
        n = len(nums)
        sum1 = n*(n+1)//2
        sum2 = sum(nums)
        return (sum1-sum2)

if __name__ == "__main__":
    nums = [9,6,4,2,3,5,7,0,1]
    sol = Solution()
    print(sol.missNum(nums))
    print(sol.missNumMath(nums))