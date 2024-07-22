
# Author: Ashish Singh

import _common_link_list as comm_funcs



class Solution:
    def mergeTwoLists(self, list1, list2):
        # if not list1 or not list2:
        #     return 
        while list2.next:
            tmp1 = list1.next
            tmp2 = list2.next
            if list1.val <= list2.val: 
                list1.next = list2
                #list2.next = tmp1
                if tmp1.val <= list2.next.val:
                    list2.next = tmp1
                list1 = tmp1
                list2 = tmp2
                else: 
                    list2.next = list1.next
                    if tmp2.val <= list2.next.val:
                        list1.next = tmp2              
                    list1 = tmp1
                    list2 = tmp2



if __name__ ==  "__main__":

    ll = comm_funcs.insertOps()
    sol = Solution()


    listNode = [1, 2, 3, 4, 5]
    for node in listNode:
        ll.insertAtLast(node)

    print(ll.addlist)

    for firstelem in ll.addlist:
        break

    print(sol.mergeTwoLists(firstelem))