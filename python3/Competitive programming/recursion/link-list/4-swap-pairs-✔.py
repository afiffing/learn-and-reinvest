# link list https://www.youtube.com/watch?v=Evm1grTr8J4
# link list https://www.youtube.com/watch?v=RhCGA4jlPmQ
# Author: Ashish Singh

import _common_link_list as comm_funcs

class Solution:
    def __init__(self):
        self.addlist = ()

    def swapPairs(self, head):
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node


if __name__ == "__main__":
    ll = comm_funcs.insertOps()
    sol = Solution()

    listNode = [1, 2, 3, 4]
    for node in listNode:
        ll.insertAtLast(node)

    print(ll.addlist)

    for first_element in ll.addlist:
        break

    # for add in ll.addlist:
    #     print(ll.swapPairs(add))

    print(sol.swapPairs(first_element))