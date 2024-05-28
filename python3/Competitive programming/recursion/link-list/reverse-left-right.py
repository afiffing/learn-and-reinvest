# Author: Ashish Singh

'''
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
|                   |
L                   R


'''

import common_link_list as comm_funcs

class Solution:

    def __init__(self, left, right) -> None:
        self.position = 0
        self.left = left
        self.right = right

    def reverseLeftRight(self, head):
 
        def helper(self, rec_head, pos):
            print(f'head at: {rec_head}')
            print(f'position: {pos}')

            if pos == self.right or not rec_head.next:
                print(f'base case met, recursion stopped {rec_head.data}')
                return rec_head
            
            if  pos < self.left-1 or pos < self.right:
                pos += 1
                print('position and head increased\n')
                rest = helper(self, rec_head.next, pos)

            return rest
        
        helper(self,head,self.position)


        

if __name__ == "__main__":
    ll = comm_funcs.insertOps()
    sol = Solution(2,5)

    listNode = [1,2,3,4,5,6]

    for node in listNode:
        ll.insertAtLast(node)

    # print(ll.addlist)    

    for elem in ll.addlist:
        break

    sol.reverseLeftRight(elem)


     
