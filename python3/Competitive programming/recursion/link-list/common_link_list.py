# link list https://www.youtube.com/watch?v=Evm1grTr8J4
# link list https://www.youtube.com/watch?v=RhCGA4jlPmQ
# Author: Ashish Singh

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class insertOps:
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