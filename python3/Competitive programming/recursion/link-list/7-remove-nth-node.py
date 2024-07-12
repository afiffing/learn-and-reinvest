
import _common_link_list as comm_funcs

class Solution:        

    def revLinkList(self,head):
        if not head or not head.next:
            return head
        rest = self.revLinkList(head.next)
        head.next.next = head
        head.next = None
        
        return rest
    
    def removeNthFromEnd(self, head, n):
        if not head.next:
            return None

        curr = self.revLinkList(head)
        prev = curr 

        temp = prev

        p=1 

        while curr:
            if n == 1:
                return self.revLinkList(curr.next)
            if p == n:
                prev.next = curr.next
                break
            else:
                pass
            p += 1
            prev = curr
            curr = curr.next
        
        print(head)
        return self.revLinkList(temp)
    

if __name__ ==  "__main__":

    ll = comm_funcs.insertOps()
    sol = Solution()


    listNode = [1, 2, 3, 4, 5]
    for node in listNode:
        ll.insertAtLast(node)

    print(ll.addlist)

    for firstelem in ll.addlist:
        break

    print(sol.removeNthFromEnd(firstelem,3))