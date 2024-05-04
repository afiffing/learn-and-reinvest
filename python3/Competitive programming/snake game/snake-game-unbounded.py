'''

Solution test case1:
    Food pops up on eating the existing one, snake eats itself in the last

snake starts at [[0,0]]
food is [[1, 2], [0, 1]]
size of the matrix is width:3, height:2

H is current head location, F is food location, B:Body, T:Tail

  0 1 2
0|H| | |
1| | |F|

sG.moveMent("R"), returns score 0, food location is [1,2]

  0 1 2
0| |H| |           #Line 50, newhead appended to path, but snake body is not increased
1| | |F|           #tail doesn't exists

sG.moveMent("D"), returns score 0

  0 1 2
0| | | |
1| |H|F|

sG.moveMent("R"), returns score 1, food location is [[0,1]]
  0 1 2
0| |F| |
1| |T|H|        #Line 44,45 score += 1 and snake body length is increased by 1
               #Tail is created.

sG.moveMent("U") returns score 2,
  0 1 2
0| |F|H|         #Line 50, newhead appended to path, but snake body is not increased
1| | |T|        #tail increased

sG.moveMent("L") returns score 2,
  0 1 2
0| |H|B|         #Line 50, newhead appended to path, snake body length is increased by 1
1| | |T|         #tail moves

sG.moveMent("U") returns score 2
  0 1 2
0| |B|T|
1| |H| |

sG.moveMent("D") returns score -1, Snake dies here.
  0 1 2
0| |X|T|
1| |B| |


'''

from collections import deque


class snakeGame:

    def __init__(self, width, height, initialPosition, food):
        self.width = width
        self.height = height
        self.foodloc = deque(food)
        self.path = deque(initialPosition)
        self.score = 0
        if self.foodloc:
            self.foodnow = self.foodloc.popleft()

    def moveMent(self, direction):

        '''
         [0,0] --> R --> [0,1]
         Right --> movement of columns
         down --> movement of rows
        '''

        head = self.path[-1]  # head is the new

        if direction == "R":
            newHead = [head[0], head[1] + 1]
        elif direction == "L":
            newHead = [head[0], head[1] - 1]
        elif direction == "D":
            newHead = [head[0] + 1, head[1]]
        elif direction == "U":
            newHead = [head[0] - 1, head[1]]
        else:
            print("Invalid direction input")

        # newHead doesn't die on edges and newhead is updated accordingly

        if newHead[0] < 0:
            newHead = [newHead[0] + self.height, newHead[1]]
        elif newHead[1] < 0:
            newHead = [newHead[0], newHead[1] + self.width]
        elif newHead[1] >= self.width:
            newHead = [newHead[0], newHead[1] - self.width]
        elif newHead[0] >= self.height:
            newHead = [newHead[0] - self.height, newHead[1]]

        # newhead is not circling back to body and tail.

        if newHead in self.path and newHead != self.path[0]:
            return -1

        if newHead == self.foodnow:  # check if food is present
            self.score += 1
            self.path.append(newHead)
            if self.foodloc:
                self.foodnow = self.foodloc.popleft()
            else:
                self.foodnow = []
        else:
            self.path.append(newHead)
            self.path.popleft()  # this will make sure that snake is moving forward

        return self.score


if __name__ == "__main__":

    directions = ["R", "D", "R", "U", "L", "U", "D"]
    initialPosition = [[0, 0]]
    foodloc = [[1, 2], [0, 1]]
    sG = snakeGame(3, 2, initialPosition, foodloc)
    scoreList = []

    print(f'Snake starting position: {initialPosition}')
    print(f'food locations: {foodloc}\n')
    for dir in directions:
        currScore = sG.moveMent(dir)
        if currScore >= 0:
            scoreList.append(currScore)
        print(f'Snake body: {sG.path}')
        print(f'Direction: {dir}\n')
        if currScore < 0:
            print(f'Snake dies, reason it ate itself')

    print(f'Final score: {scoreList[-1]}')