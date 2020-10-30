"""
Detect a cycle in linked list
"""
from Single_Linked_List import Single_Linked_List, Node

def detect_cycle(sll):
    visited_nodes=[]
    root=sll.head
    while(root!=None):
        if root in visited_nodes:
            return True
        visited_nodes.append(root)
        root=root.get_next()
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
    # fourth_node.set_next(first_node)
    result=detect_cycle(root1)
    print("Is cycle present in our linked list",result)