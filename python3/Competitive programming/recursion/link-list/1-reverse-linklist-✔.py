# link list https://www.youtube.com/watch?v=Evm1grTr8J4
# link list https://www.youtube.com/watch?v=RhCGA4jlPmQ
# Author: Ashish Singh

import _common_link_list as comm_funcs

class Solution:
    def __init__(self):
        self.head = None

    def reversal(self, head):  
        if not head or not head.next:
            return head
        rest = self.reversal(head.next)
        head.next.next = head
        head.next = None
        return rest


if __name__ == "__main__":
    ll = comm_funcs.insertOps()
    sol = Solution()

    listNode = [1, 2, 3, 4]
    for node in listNode:
        ll.insertAtLast(node)

    print(ll.addlist)

    for first_element in ll.addlist:
        break

    print(sol.reversal(first_element))

    ll.addlist = ()

    for node in listNode:
        ll.insertAtBeginning(node)
    
    print(ll.addlist)

    for first_element in ll.addlist:
        break

    print(sol.reversal(first_element))
