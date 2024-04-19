# Author: Ashish Singh
# Logger rate limit, each unique message should only be printed at-most every Y seconds
# We will use a hashmap to store only those messages, which are unique and a

import time


class Logger:
    def __init__(self):
        self.msg_dict = {}

    def shouldPrintMsg(self, msg, timeStamp, coolOffPeriod):
        print(msg,timeStamp)
        if self.msg_dict.get(msg, 0) > timeStamp:
            return False
        self.msg_dict[msg] = timeStamp + coolOffPeriod
        print(self.msg_dict)
        return True


if __name__ == '__main__':
    data = ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage",
            "shouldPrintMessage", "shouldPrintMessage"]
    obj = Logger()
    outputList = []

    for msg in data:
        time.sleep(0.5)
        outputList.append(obj.shouldPrintMsg(msg, time.time(), 0.6))

    print(data)
    print(outputList)
