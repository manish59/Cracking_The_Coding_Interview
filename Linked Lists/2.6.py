"""
Check if the linked list is a palindrome
"""

from Single_Linked_List import Single_Linked_List, Node as SLLNode

def reverse_list(sll):
    root=sll.head
    new_root=Single_Linked_List()
    while(root!=None):
        print(root.data)
        node=SLLNode(root.data)
        new_root.add_front(node)
        root=root.get_next()
    return new_root
def compare(sll1,sll2):
    root1=sll1.head
    root2=sll2.head
    while(root1!=None):
        if root1.data!=root2.data:
            return False
        root1=root1.get_next()
        root2=root2.get_next()
    return True
if __name__=="__main__":
    root=Single_Linked_List()
    temp=root
    for i in [1,2,3,2,1]:
        temp.append(SLLNode(i))
    root.print_list()
    reverse=reverse_list(root)
    reverse.print_list()
    print(compare(root,reverse))