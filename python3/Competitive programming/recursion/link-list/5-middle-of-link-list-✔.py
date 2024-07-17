# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/ 
# Author: Ashish Singh

import _common_link_list as comm_funcs

class Solution:
    def __init__(self):
        self.addlist = ()

    def findMiddle(self, head):
       
       curr = head
       len = 0
       while curr:
        curr = curr.next
        len += 1
      
       if len <= 1:
          return head
       else:
          n = int(len/2) + 1

       p = 0 
       curr = head

       while curr:
        p += 1
        if p == n:
           break
        else:
           pass
        curr = curr.next
           
       return curr

    def findMiddle2(self, head):
       slow = fast = head
       while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
           
       return slow

if __name__ == "__main__":
    ll = comm_funcs.insertOps()
    sol = Solution()

    listNode = [1, 2, 3, 4]
    for node in listNode:
        ll.insertAtLast(node)

    print(ll.addlist)

    for first_element in ll.addlist:
        break

    print(sol.findMiddle(first_element))