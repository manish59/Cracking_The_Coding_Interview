class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Signle_Linked_List_Stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
    def pop(self):
        popped_node=self.head
