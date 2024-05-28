# Author: Ashish Singh
# Approach is Divide and Conquer


class Solution:
    def reverseStr(self, s):
        def helper(left, right):
            if left < right:
                s[left],s[right] = s[right],s[left]
                helper(left+1,right-1)
        helper(0,len(s)-1)


if __name__ == "__main__":
    s = [ "h","e","l", "l","o"]
    sol = Solution()

    sol.reverseStr(s)
    print(s)

