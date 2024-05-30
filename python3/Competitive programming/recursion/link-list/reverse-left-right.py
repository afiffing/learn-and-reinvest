# Author: Ashish Singh

import common_link_list as comm_funcs

class Solution:

    def __init__(self, left, right) -> None:
        self.position = 0
        self.prev = None
        self.left = left
        self.right = right

    def reverseBetween(self, head):
 
        def helper(self, rec_head, pos):
            print(f'\npos: {pos}')
            print(f'recursion entered: {rec_head.data}')

            if pos == self.right-1:
                return rec_head

            if pos < self.right-1:
                pos += 1
                print(f'recursion called : {rec_head.next.data}' )

                rest = helper(self, rec_head.next, pos)
                rec_head.next.next = rec_head
                print(f'\n{rec_head.next.data} --> {rec_head.data}')

                print(f'rest data: {rest.data}')
                return rest

        if  self.position < self.left-1:
            self.position += 1
            self.prev = head
            head = head.next
            self.reverseBetween(head)              
        else:
            self.prev.next=helper(self,head,self.position)
            print(f'{self.prev.data} --> {self.prev.next.data}')

        
        return self.prev.data

if __name__ == "__main__":
    ll = comm_funcs.insertOps()
    sol = Solution(2,4)

    listNode = [1,2,3,4,5]

    for node in listNode:
        ll.insertAtLast(node)

    # print(ll.addlist)    

    for elem in ll.addlist:
        break

    print(listNode)
    sol.reverseBetween(elem)


     
