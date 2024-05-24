# link list https://www.youtube.com/watch?v=Evm1grTr8J4
# link list https://www.youtube.com/watch?v=RhCGA4jlPmQ
# Author: Ashish Singh

import common_link_list as comm_funcs

class Solution:
    def __init__(self):
        self.head = None

    def reversal(self, head):  # local head reference
        if not head or not head.next:  # base condition for last element while reversal.
            return f'head is at {head.data}, {head}'
        '''
        1 -> [ 2 -> rest of the list -> None]
        |
        head

        None <- 1 <- [ 2 -> rest of the list -> None]
                       |
                      head       

        '''
        print(f'recursion call for: {head.next.data}')
        rest = self.reversal(head.next)
        head.next.next = head
        print(f'{head.next.data} --> {head.data}--> None')
        head.next = None
        return rest  # 1


if __name__ == "__main__":
    sol = Solution()
    listNode = [1, 2, 3, 4]
    for node in listNode:
        comm_funcs.insertAtBeginning(node)

    print("################# --> insert at beginning")
    print(comm_funcs.addlist)

    for first_head in comm_funcs.addlist:
        break

    print("################# reversal by recursion")
    print(sol.reversal(first_head))

    print("################# insert at last <--")

    comm_funcs.addlist = ()

    for node in listNode:
        comm_funcs.insertAtLast(node)

    print(comm_funcs.addlist)

    for first_head in comm_funcs.addlist:
        break

    print("################# reversal by recursion")
    print(sol.reversal(first_head))