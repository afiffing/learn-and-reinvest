class solution:
    def __init__(self):
        self.memo = {}

    def robHouse(self, nums):
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            if i not in self.memo:
                self.memo[i] = max(dp(i - 2) + nums[i], dp(i - 1))
            return self.memo[i]

        return dp(len(nums) - 1)


if __name__ == "__main__":
    #nums = [1, 2, 3, 1]
    nums = [2,7,9,3,1]
    sol = solution()
    print(sol.robHouse(nums))
