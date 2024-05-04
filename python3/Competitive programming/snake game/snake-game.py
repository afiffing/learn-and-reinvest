#Author: Ashish singh
#Snake game is deque for food and path
#directions conditions, game over conditions
#return score

from collections import deque

class snakeGame:
    def __init__(self, width, height, food):
        self.width = width
        self.height = height
        self.score = 0
        self.path = deque([[0, 0]])
        self.foodloc = deque(food)
        if self.foodloc:
            self.foodnow = self.foodloc.popleft()

    def move(self, direction):
        head = self.path[-1]

        if direction == "R":
            newHead = [head[0],head[1]+1]
        elif direction == "D":
            newHead = [head[0]+1,head[1]]
        elif direction == "L":
            newHead = [head[0],head[1]-1]
        elif direction == "U":
            newHead = [head[0]-1,head[1]]
        else:
            print("please provide the correc input")

        if  newHead[0] < 0 or newHead[0] >= self.height or newHead[1] >= self.width or newHead[1] < 0:
            return -1

        if newHead in self.path and newHead != self.path[0]:
            return -1

        if newHead == self.foodnow:
            self.score += 1
            self.path.append(newHead)
            if self.foodloc:
                self.foodnow = self.foodloc.popleft()
            else:
                self.foodnow = []
        else:
            self.path.append(newHead)
            self.path.popleft()
        return self.score


if __name__ == "__main__":
    directions = ["R", "D", "R", "U", "L", "U"]
    sG = snakeGame(3,2,[[1, 2], [0, 1]])
    opList = []
    for dir in directions:
        opList.append(sG.move(dir))

    print(opList)
