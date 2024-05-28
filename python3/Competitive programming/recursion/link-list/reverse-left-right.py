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
            print(f'position: {pos}')
            if pos == self.right or not rec_head.next:
                return rec_head
            elif pos < self.right:
                print(f'element passed {rec_head.data}')
                pos += 1
                rest = helper(self,rec_head.next,pos)
                rec_head.next.next = rec_head   
                '''
                1-2-3-4-5-6
                1-2-3-4->5->6
                '''
            return rest

        if self.left == self.right:
            return head
        if self.position < self.left-1:
            self.position += 1
            print(self.position)
            head = head.next
        else:
            helper(self, head.next, self.position)
        

if __name__ == "__main__":
    ll = comm_funcs.insertOps()
    sol = Solution(1,5)

    listNode = [1,2,3,4,5,6]

    for node in listNode:
        ll.insertAtLast(node)

    print(ll.addlist)    

    for elem in ll.addlist:
        break

    sol.reverseLeftRight(elem)

     
