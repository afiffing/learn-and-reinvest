# link list https://www.youtube.com/watch?v=Evm1grTr8J4
# link list https://www.youtube.com/watch?v=RhCGA4jlPmQ
# Author: Ashish Singh

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def __init__(self):
        self.current = None
        self.linklist = []
        self.addlist = ()

    def traverseNode(self, data):
        newnode = Node(data)  # address of new node, node.data = 10, node.next = None
        self.addlist = self.addlist + (newnode,)
        print(f"address of new node i.e. {newnode.data}: {newnode}")

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

    def swapPairs(self, head):
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next

        first_node.next = self.swapPairs(second_node.next)

        second_node.next = first_node

        return second_node


if __name__ == "__main__":
    ll = Solution()
    listNode = [1, 2, 3, 4]
    for node in listNode:
        ll.traverseNode(node)

    print(ll.addlist)

    for add in ll.addlist:
        print(ll.swapPairs(add))
