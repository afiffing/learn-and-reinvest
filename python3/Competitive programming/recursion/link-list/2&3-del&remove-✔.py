
import _common_link_list as comm_funcs


if __name__ == "__main__":

    ll = comm_funcs.insertOps()

    list = [1,2,3,4,5]

    for a in list:
        ll.insertAtBeginning(a)
    
    print(ll.addlist)

    for elem in ll.addlist:
        break

    print(type(elem))

    dl = comm_funcs.delOps

    print(dl.delLegacyWay(dl,elem,3))