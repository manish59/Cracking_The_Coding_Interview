from Single_Linked_List import Single_Linked_List,Node as SLLNode
from Double_Linked_List import Double_Linked_List,Node as DLLNode

def remove_duplicates_sll(sll):
    data=[]
    current=sll.head
    prev=None
    while(current!=None):
        if current.get_data() not in data:
            data.append(current.get_data())
            prev = current
        else:
            prev.set_next(current.get_next())
        current=current.get_next()
def remove_duplicates_dll(dll):
    data=[]
    current=dll.head
    prev=None
    while(current!=None):
        if current.get_data() not in data:
            data.append(current.get_data())
            prev=current
        else:
            prev.set_next(current.get_next())
            if current.get_next() is not None:
                current.get_next().set_prev(prev)
        current=current.get_next()
if __name__=="__main__":
    DLL=Double_Linked_List()
    SLL=Single_Linked_List()
    for i in [1,2,3,4,5,6,7,6,5,4,3,2,1]:
        DLL.append(DLLNode(i))
        SLL.append(SLLNode(i))
    remove_duplicates_sll(SLL)
    SLL.print_list()
    print("##########################")
    remove_duplicates_dll(DLL)
    DLL.print_list()