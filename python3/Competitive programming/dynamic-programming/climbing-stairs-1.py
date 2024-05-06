# classic dynamic programming
# top down with memoization

# max/min/number of ways/best possible/how many ways
# first figure out relevant state
# construct the structure/function
# look for reoccurence, form recursion
# base condition
# memoization


class solution:

    def __init__(self):
        self.memo = {}

    def climbStairs(self, n):

        def dp(i):  # i is the current state of which stairs
            # 30 step
            if i < 3:
                return i

            if i not in self.memo:
                self.memo[i] = dp(i - 1) + dp(i - 2)

            return self.memo[i]

        return dp(n)


if __name__ == "__main__":
    sol = solution()
    print(sol.climbStairs(3))
