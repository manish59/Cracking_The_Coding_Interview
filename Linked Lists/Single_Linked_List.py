class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return "Node object: data{}".format(self.data)
    def get_data(self):
        return self.data
    def set_data(self,data):
        self.data=data
    def get_next(self):
        return self.next
    def set_next(self,new_node):
        self.next=new_node
class Single_Linked_List:
    def __init__(self):
        self.head=None
    def __repr__(self):
        return f"Single Linked List head :{self.head}"
    def is_empty(self):
        return self.head is None
    def add_front(self,node):
        if self.head==None:
            self.head=node
        else:
            first_node=self.head
            self.head=node
            node.set_next(first_node)
    def size(self):
        count=0
        if not self.is_empty():
            temp=self.head
            while(temp!=None):
                count +=1
                temp=temp.get_next()
        else:
            count="Single Linked List is empty"
        return count
    def search(self,data):
        temp=self.head
        while(temp!=None):
            if temp.data==data:
                return True
            temp=temp.get_next()
        return False
    def print_list(self):
        temp=self.head
        if self.head is None:
            return "Single Linked List is empty"
        while(temp!=None):
            print(temp.get_data())
            temp=temp.get_next()
    def append(self,node):
        temp=self.head
        if self.head==None:
            self.head=node
            node.set_next(temp)
            return
        else:
            while(temp.next!=None):
                temp=temp.get_next()
            temp.set_next(node)
            return
        print(f"Added Node to Linked List {node.data}")
    def pop(self):
        temp=self.head
        while(temp.next.next!=None):
            temp=temp.get_next()
        data=temp.next.data
        temp.next=None
        return data
    def pop_front(self):
        temp=self.head
        self.head=self.head.next
        return temp.data
    def remove(self,data):
        if self.head is None:
            return "Single Linked List is empty"
        current=self.head
        prev_node=None
        found=False
        while not found:
            if current.get_data()==data:
                found=True
            else:
                if current.get_next()==None:
                    return "Node with any is found in our Single Linked List"
                else:
                    prev_node=current
                    current=current.get_next()
        print(prev_node)
        if prev_node==None:
            self.head=current.get_next()
        else:
            prev_node.set_next(current.get_next())
if __name__=="__main__":
    SLL=Single_Linked_List()
    # print(SLL.remove(11))
    # for i in range(10):
    #     SLL.add_front(Node(i))
    # for i in range(10,20):
    #     SLL.append(Node(i))
    # SLL.print_list()
    # SLL.remove(11)
    # print("###")
    # SLL.print_list()