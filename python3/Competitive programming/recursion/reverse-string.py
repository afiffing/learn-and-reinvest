# Author: Ashish Singh
# Approach is Divide and Conquer


class Solution():
    def revString(self,s):

        def helper(left,right):
            if left < right:
                s[left],s[right] = s[right], s[left]
                helper(left+1,right-1)
        helper(0,len(s)-1)

if __name__ == "__main__":
    s1 = Solution()
    strList = [x for x in 'hello']
    s1.revString(strList)
    print(''.join(strList))


