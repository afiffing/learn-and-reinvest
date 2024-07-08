#Author: Ashish Singh
#Idea is to match values with an 

import _common_link_list as comm_funcs


class Solution():
    def __init__(self):
        self.head = None
    
    def isPalindrome(self, head):

        self.fp = head

        return self.solve(head)

    def solve(self, head):
        if head is None:
            return True
        ans = self.solve(head.next) and self.fp.data == head.data
        self.fp = self.fp.next
        return ans 

if __name__ == "__main__":
    ll = comm_funcs.insertOps()
   
    sol = Solution()

    '''
    Insertion at the last

    '''

    listNode = [1, 2, 2, 1]
    for node in listNode:
        ll.insertAtLast(node)

    print(ll.addlist)

    for first_element in ll.addlist:
        break

    print(sol.isPalindrome(first_element))

    '''
    Insertion at the beginining

    '''
    
    ll.addlist = ()

    for node in listNode:
        ll.insertAtBeginning(node)
    
    print(ll.addlist)

    for first_element in ll.addlist:
        break

    print(sol.isPalindrome(first_element))
