# class solution:
#     def __init__(self, val=0, next=1):
#         self.val = val
#         self.next = next
#
#     def swapPairs(self, head):
#
#         def helper(val, next):
#             if len(head) <= 1:
#                 return head
#
#             if len(head) % 2 != 0:
#                 return head
#
#             head[val], head[next] = head[next], head[val]
#             print(head)
#             if val + 2 < len(head):
#                 helper(val + 2, next + 2)
#
#         return helper(self.val, self.next)
#
#
# if __name__ == "__main__":
#     head = [1,2,3,4,5]
#     sol = solution()
#     print(sol.swapPairs(head))


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.current = None
        self.linklist = []
        self.position = 0

    def traverseNode(self, data):
        newnode = Node(data)  # address of new node, node.data = 10, node.next = None
        print(f"address of new node i.e. {newnode.data}: {newnode}")
        #        print(f"next of {newnode.data}: {newnode.next}")

        if self.current is None:
            self.current = newnode
            print("newnode current is none")
            return
        else:
            self.current.next = newnode  # current next is updated with new node
            '''
            1 --> address of 2
            |
            current

            append in the list for visual reference.     

            1 --> address of 2
                    |
                 current
            '''
            # print(f"next of {newnode.data}: {newnode.next}")

            self.linklist.append(f"{self.current.data} --> {self.current.next}")
            self.current = newnode
            self.position += 1
            if (self.position) % 2 == 0:
                print(self.position)

    def insertNode(self, position, data):
        if position == 0:
            self.traverseNode(data)
        else:
            print("can't insert")


if __name__ == "__main__":
    nodedata = [1, 2, 3, 4]
    ll = LinkedList()
    for data in nodedata:
        ll.traverseNode(data)
    print(ll.linklist)

    ll.insertNode(0, 5)

# self.current = None, newnode = Node(10),
# self.current = Node(10), newnode = Node(20)


# if self.head is None:
#     self.head = new_node
#     return
# else:
#     new_node.next = self.head
#     self.head = new_node
