from Single_Linked_List import *
def setup(data):
    sll=Single_Linked_List()
    for i in data:
        sll.append(Node(i))
    return sll

def partition(sll,element):
    p1=sll.head
    parition_linked_list=Single_Linked_List()
    while(p1 is not None):
        if p1.get_data()<element:
            parition_linked_list.append(Node(p1.get_data()))
        p1=p1.get_next()
    p1=sll.head
    while(p1 is not None):
        if p1.get_data()>=element:
            parition_linked_list.append(Node(p1.get_data()))
        p1=p1.get_next()
    return parition_linked_list
if __name__=="__main__":
    sll=setup([1,2,3,4,5,6,7,8,9,7,5,4,4,65,6,5,43,56,43,3,5,4,3,56,4,3,56,54,4])
    pll=partition(sll,5)
    sll.print_list()
    print("##################")
    pll.print_list()