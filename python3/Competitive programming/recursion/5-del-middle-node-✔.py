# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/ 
# Author: Ashish Singh

import _common_link_list as comm_funcs

class Solution:
    def __init__(self):
        self.addlist = ()

    def delMiddle(self, head):
       
       curr = head
       position = 0
       while curr:
        curr = curr.next
        position += 1
      
       if position <= 1:
          return head
       else:
          n = int(position/2) 

       p = 0 
       prev, curr = head, head

       while curr:
        if p == n:
           prev.next = curr.next
           break
        else:
           pass
        p += 1
        prev = curr
        curr = curr.next
           
       return head


if __name__ == "__main__":
    ll = comm_funcs.insertOps()
    sol = Solution()

    listNode = [1, 2, 3, 4]
    for node in listNode:
        ll.insertAtLast(node)

    print(ll.addlist)

    for first_element in ll.addlist:
        break

    print(sol.delMiddle(first_element))