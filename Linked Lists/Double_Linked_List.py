class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    def __repr__(self):
        return "Node object: data {}".format(self.data)
    def get_data(self):
        return self.data
    def set_data(self,data):
        self.data=data
    def set_next(self,new_node):
        self.next=new_node
    def get_next(self):
        return self.next
    def get_prev(self):
        return self.prev
    def set_prev(self,new_node):
        self.prev=new_node
class Double_Linked_List:
    def __init__(self):
        self.head=None
    def print_list(self):
        current=self.head
        if self.head==None:
            return "Double Linked List is empty"
        while(current is not None):
            print(current.get_data())
            current=current.get_next()
    def add_front(self,node):
        if self.head==None:
            self.head=node
            node.set_prev(self.head)
        else:
            first_node=self.head
            self.head=node
            node.set_next(first_node)
            node.set_prev(self.head)
            first_node.set_prev(node)
    def append(self,node):
        if self.head==None:
            self.head=node
            node.set_prev(self.head)
        else:
            current=self.head
            while(current.next is not None):
                current=current.get_next()
            current.set_next(node)
            node.set_prev(current)
    def size(self):
        count=0
        if self.head==None:
            return "Double Linked List is empty"
        else:
            current=self.head
            while(current is not None):
                count=count+1
                current=current.get_next()
            return count
    def pop(self):
        if self.head==None:
            return "No more elements in DLL because it is empty"
        else:
            current=self.head
            prev=None
            while(current.get_next()!=None):
                prev=current
                current=current.get_next()
            if prev==None:
                self.head=current.get_next()
                current.get_next().set_prev(self.head)
                return current.get_data()
            else:
                data=current.get_data()
                print("Previous Data",data)
                print("Current Data",current.data)
                prev.set_next(None)
                return data
    def remove(self,data):
        if self.head==None:
            return "List empty, not found"
        else:
            found=False
            prev=None
            current=self.head
            while not found:
                if current.get_data()==data:
                    found=True
                else:
                    prev=current
                    current=current.get_next()
                    if current==None:
                        return "Element not found, reached end of the list"
            if prev==None:
                self.head=current.get_next()
                if current.get_next()!=None:
                    current.get_next().set_prev(self.head)
            else:
                prev.set_next(current.get_next())
                current.get_next().set_prev(prev)

if __name__=="__main__":
    DLL=Double_Linked_List()
    DLL.add_front(Node(1))
    DLL.add_front(Node(2))
    DLL.add_front(Node(3))
    DLL.add_front(Node(4))
    DLL.print_list()