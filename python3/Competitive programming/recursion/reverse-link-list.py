# link list https://www.youtube.com/watch?v=Evm1grTr8J4
# link list https://www.youtube.com/watch?v=RhCGA4jlPmQ
# Author: Ashish Singh

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def __init__(self):
        self.head = None
        self.addlist = ()

    def insertAtLast(self, data):
        newnode = Node(data)  # address of new node, node.data = 10, node.next = None
        print(f"address of new node i.e. {newnode.data}: {newnode}")

        self.addlist = self.addlist + (newnode,)
        if self.head is None:
            self.head = newnode
            return
        else:
            self.head.next = newnode  # current next is updated with new node
            '''
            1 --> address of 2
            |
            head

            append in the list for visual reference.     

            1 --> address of 2
                    |
                  head
            '''
            self.head = newnode

    def insertAtBeginning(self, data):
        newnode = Node(data)
        print(f"address of new node i.e. {newnode.data}: {newnode}")
        newnode.next = self.head
        self.head = newnode
        self.addlist = (newnode,) + self.addlist

        return self.head

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
    ll = Solution()
    listNode = [1, 2, 3, 4]
    for node in listNode:
        ll.insertAtBeginning(node)

    print("################# --> insert at beginning")
    print(ll.addlist)

    for first_head in ll.addlist:
        break

    print("################# reversal by recursion")
    print(ll.reversal(first_head))

    print("################# insert at last <--")

    ll.addlist = ()

    for node in listNode:
        ll.insertAtLast(node)

    print(ll.addlist)

    for first_head in ll.addlist:
        break

    print("################# reversal by recursion")
    print(ll.reversal(first_head))