class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None
    def print_linked_list(self):
        temp=self.head
        while(temp!=None):   
            print(temp.data)
            temp=temp.next
def delete_linked_node(linked_list,nth_node):
    i=0
    temp=linked_list.head
    prev_node=None
    while(temp!=None):
        i=1
        if i==nth_node:
            temp.next=temp.next.next
        temp=temp.next
if __name__=="__main__":
    single_link=SingleLinkedList()
    first_node=Node(4)
    single_link.head=first_node
    second_node=Node(5)
    first_node.next=second_node
    third_node=Node(6)
    second_node.next=third_node
    fouth_node=Node(7)
    third_node.next=fouth_node
    # single_link.print_linked_list()
    delete_linked_node(single_link,3)
    single_link.print_linked_list()
