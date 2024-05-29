# Author: Ashish Singh

import common_link_list as comm_funcs

class Solution:

    def __init__(self, left, right) -> None:
        self.position = 0
        self.left = left
        self.right = right

    def reverseLeftRight(self, head):
 
        def helper(self, rec_head, pos):
            print(f'head at: {rec_head.data}')
            print(f'position: {pos}')

            if pos == self.right or not rec_head.next:
                print(f'base case met, recursion stopped {rec_head.data-1}')
                return rec_head

            if pos < self.right:
                pos += 1
                print('reversal started\n')
                rest = helper(self, rec_head.next, pos)
                rec_head.next.next = rec_head
                print(f'{rec_head.next.data} --> {rec_head.data}')

                return rest

        if  self.position < self.left-1:
            self.position += 1
            print('position and head increased\n')
            head = head.next 
            self.reverseLeftRight(head)              
        else:
            helper(self,head.next,self.position)


if __name__ == "__main__":
    ll = comm_funcs.insertOps()
    sol = Solution(1,4)

    listNode = [1,2,3,4,5,6]

    for node in listNode:
        ll.insertAtLast(node)

    # print(ll.addlist)    

    for elem in ll.addlist:
        break

    sol.reverseLeftRight(elem)


     
