from Single_Linked_List import *

def setup_sll(limit):
    root=Single_Linked_List()
    for i in range(limit):
        root.append(Node(i))
    return root
def get_nth_element_from_last(sll,n):
    p1=sll.head
    p2=sll.head
    count=0
    for i in range(n):
        p1=p1.get_next()
        count +=1
    while(p1 is not None):
        p1=p1.get_next()
        p2=p2.get_next()
        count +=1
    if count<n:
        return "No Data Found list is smaller than the nth element"
    return p2.get_data()
if __name__=="__main__":
    sll=setup_sll(10)
    result=get_nth_element_from_last(sll,4)
    print(result)
