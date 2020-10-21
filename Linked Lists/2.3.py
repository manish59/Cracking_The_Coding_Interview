from Single_Linked_List import *
def setup(limit):
    sll=Single_Linked_List()
    for i in range(1,limit):
        sll.append(Node(i))
    return sll
def delete_middle_node(sll):
    root=sll.head
    size=sll.size()
    middle_node=int(size/2)-1
    for i in range(middle_node):
        root=root.get_next()
    root.set_next(root.get_next().get_next())

if __name__=="__main__":
    sll=setup(11)
    delete_middle_node(sll)
    sll.print_list()