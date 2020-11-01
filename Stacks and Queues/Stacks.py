"""
Implementing Stacks
"""

class Stack:
    def __init__(self):
        self.array=[]
    def pop(self):
        if len(self.array)>0:
            return self.array.pop()
        else:
            return "Stack Empty"
    def push(self,element):
        self.array.append(element)
    def peek(self):
        if len(self.array)>0:
            return self.array[-1]
        else:
            return "Stack Empty"
    def isEmpty(self):
        if len(self.array)==0:
            return True
        return False
    def print_stack(self):
        print(*self.array,sep=",")
if __name__=="__main__":
    storage=Stack()
    print(storage.peek())
    print(storage.isEmpty())
    print(storage.pop())
    storage.push(1)
    storage.push(2)
    storage.push(3)
    print(storage.peek())
    storage.print_stack()