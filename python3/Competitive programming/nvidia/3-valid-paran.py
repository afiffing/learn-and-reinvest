#Author Ashish Singh
# Key element is to check if stack is filled, or odd one paranthesis left in the stack. It should always be a pair.


class Solution():
    def __init__(self):
        self.map = {'}':'{', ')':'(',']':'['}
        self.stack = []

    
    def isValid(self,s):
        for elem in s:
            if elem in self.map.values():
                self.stack.append(elem)
            elif elem in self.map.keys():
                if not self.stack or self.map[elem] != self.stack.pop():
                    return False
        return not self.stack


if __name__ == "__main__":
    sol = Solution()
    s = "(){"
    print(sol.isValid(s))