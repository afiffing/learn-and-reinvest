#WIP
#Author: Ashish Singh

from collections import deque


class posInt:
    def __init__(self, initArr):
        self.deque = deque(maxlen=len(initArr))
    #
    # def check(self):
    #     self.deque.popleft()
    #     print(self.deque)


if __name__ == "__main__":

    ipArr = [10, 12, 2, 6, 14,18]
    print(sorted(ipArr))
    setLen = int(len(ipArr)/2)
    print(setLen)

    ch = posInt(ipArr)

    # for item in range(len(ipArr)):
    #     ch.check()





