from Single_Linked_List import *
def setup(data):
    sll=Single_Linked_List()
    for i in data:
        sll.append(Node(i))
    return sll
def sum_linked_list(a,b):
    s1=a.head
    s2=b.head
    result=Single_Linked_List()
    carry=0
    while(s1 is not None):
        current_sum=s1.get_data()+s2.get_data()+carry
        print("current_sum",current_sum)
        if current_sum<10:
            result.add_front(Node(current_sum))
        else:
            node_value=current_sum%10
            carry=int(current_sum/10)
            result.add_front(Node(node_value))
        s1=s1.get_next()
        s2=s2.get_next()
    return result
if __name__=="__main__":
    s1=setup([7,1,6])
    s2=setup([5,9,2])
    print(s1.print_list())
    print(s2.print_list())
    result=sum_linked_list(s1,s2)
    result.print_list()