class Solution:
    
    def recur(self,h):
        h.val, h.next.val = h.next.val, h.val
        return h


    def sortList(self, head):
        if not head:
            return head
        while head:
            if head.val > head.next.val:
                head = self.recur(head)
            else:
                head = head.next
            

        return None


if __name__ ==  "__main__":

    ll = comm_funcs.insertOps()
    sol = Solution()


    listNode = [1, 2, 3, 4, 5]
    for node in listNode:
        ll.insertAtLast(node)

    print(ll.addlist)

    for firstelem in ll.addlist:
        break

    print(sol.sortList(firstelem))