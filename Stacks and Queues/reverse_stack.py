from Stacks import Stack
def reverse(stack):
    if stack.isEmpty()!=True:
        temp=stack.pop()
        reverse(stack)
        print(temp)
        insert_at_bottom(stack,temp)
def reverse_stack(stack):
    new_stack=Stack()
    while(stack.isEmpty() is not True):
        new_stack.push(stack.pop())
    return new_stack
def insert_at_bottom(stack,element):
    if stack.isEmpty():
        stack.push(element)
    else:
        temp=stack.pop()
        insert_at_bottom(stack,element)
        stack.push(temp)
if __name__=="__main__":
    array=Stack()
    array.push(1)
    array.push(2)
    array.push(3)
    array.push(4)
    array.push(5)
    array.push(6)
    array.print_stack()
    reverse(array)
    array.print_stack()