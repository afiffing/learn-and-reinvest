from collections import deque

class Solution():

    def __init__(self) -> None:
        #self.stringStack = []
        self.deque = deque()
        self.maxlength = 0

    def lengthOfLongestSubstring(self,s):
        if not s:
            return 0
        
        for char in s:
            print(char)
            if char not in self.deque:
                self.deque.append(char)
                print(self.deque)
            else: 
                while char in self.deque:
                    self.deque.popleft()
                self.deque.append(char)
                print(self.deque)
            self.maxlength = max(self.maxlength,len(self.deque))
    
        return self.maxlength

                        
    

    
if __name__  == "__main__":
    s1 = Solution()
    #s = "abcabcbb"
    #s = "pwwkew"
    s = "dvdf"

    print(s1.lengthOfLongestSubstring(s))

