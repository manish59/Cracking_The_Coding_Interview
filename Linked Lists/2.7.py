"""
Intersection of two linked lists check it out
"""
from Single_Linked_List import Single_Linked_List, Node

def check_intersection(sll1,sll2):
    root1=sll1.head
    root2=sll2.head
    while(root1!=None):
        while(root2!=None):
            print(root1.data, root2.data)
            if root1==root2:
                return True
            root2=root2.get_next()
        root2=sll2.head
        root1=root1.get_next()
    return False

if __name__=="__main__":
    root1=Single_Linked_List()
    "1->2>3>4>1>2>3"
    first_node=Node(1)
    second_node=Node(2)
    third_node=Node(3)
    fourth_node=Node(4)
    root1.head=first_node
    first_node.set_next(second_node)
    second_node.set_next(third_node)
    third_node.set_next(fourth_node)
    root2=Single_Linked_List()
    f1=Node(1)
    f2=Node(2)
    f3=Node(3)
    root2.head=f1
    f1.set_next(f2)
    # f2.set_next(fourth_node)
    print(root1.print_list())
    print(root2.print_list())
    result=check_intersection(root1,root2)
    print(result)