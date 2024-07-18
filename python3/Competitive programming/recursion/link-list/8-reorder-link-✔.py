# Author: Ashish Singh

import _common_link_list as comm_funcs

class Solution:

    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """

        #base condition
        if not head:
            return head
        
        # find middle of the link list
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #revere by iteration
        prev, curr = None, slow

        while curr:
            curr.next, prev, curr  = prev, curr, curr.next
        
        #merge two sorted lists
        first, second = head, prev
        while second.next:
            tmp = first.next
            first.next = second
            first = tmp

            tmp = second.next
            second.next = first
            second = tmp

        return head
    

if __name__ ==  "__main__":

    ll = comm_funcs.insertOps()
    sol = Solution()


    listNode = [1, 2, 3, 4, 5]
    for node in listNode:
        ll.insertAtLast(node)

    print(ll.addlist)

    for firstelem in ll.addlist:
        break

    print(sol.reorderList(firstelem))