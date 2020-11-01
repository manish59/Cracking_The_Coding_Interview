"""
Implement three stacks using a single array
"""

class Stack:
    def __init__(self,size):
        self.size=size
        self.array=[None]*size
        self.top1=None
        self.top2=None
        self.top3=None
    def peek_stack1(self):
        return self.top1
    def peek_stack2(self):
        return self.top2
    def peek_stack3(self):
        return self.top3
    def push(self,start,end,data,top):
        for i in range(end-1,start-1,-1):
            if self.array[i]==None:
                self.array[i]=data
                top=data
                break
            continue
    def pop(self,start,end,top):
        for i in range(start,end):
            value=self.array[i]
            if value!=None:
                self.array[i]=None
                if start-1>=0:
                    top=self.array[i-1]
                else:
                    top=self.array[start]
                return value
        return "Stack is Empty"
    def pop_stack1(self):
        array_start = 0
        array_end = int(len(self.array) / 3)
        return self.pop(array_start,array_end,self.top1)
    def pop_stack2(self):
        array_start = int((len(self.array) / 3))
        array_end = int(2 * (len(self.array) / 3))
        return self.pop(array_start,array_end,self.top2)
    def pop_stack3(self):
        array_start = int(2 * (len(self.array) / 3))
        array_end = len(self.array)
        return self.pop(array_start,array_end,self.top3)
    def push_stack1(self,data):
        array_start=0
        array_end=int(len(self.array)/3)
        self.push(array_start,array_end,data,self.top1)
    def push_stack2(self,data):
        array_start=int((len(self.array)/3))
        array_end=int(2*(len(self.array)/3))
        self.top1 = array_end
        self.push(array_start, array_end, data,self.top2)
    def push_stack3(self,data):
        array_start=int(2*(len(self.array)/3))
        array_end=len(self.array)
        self.top1 = array_end
        self.push(array_start, array_end, data,self.top3)
    def print_list(self):
        print(*self.array,sep=",")
if __name__=="__main__":
    array=Stack(10)
    array.push_stack1(1)
    print(array.peek_stack1())
    array.push_stack1(2)
    print(array.peek_stack1())
    array.push_stack1(3)
    print(array.peek_stack1())
    array.push_stack1(4)
    print(array.peek_stack1())
    array.push_stack2(4)
    print(array.peek_stack1())
    array.push_stack2(5)
    print(array.peek_stack1())
    array.push_stack2(6)
    print(array.peek_stack1())
    array.push_stack3(7)
    array.push_stack3(8)
    array.push_stack3(9)
    array.push_stack3(10)
    array.print_list()
    print(array.pop_stack1())
    array.print_list()
    print(array.pop_stack1())
    array.print_list()
    print(array.pop_stack1())
    array.print_list()
    print(array.pop_stack1())
    array.print_list()
    print(array.pop_stack2())
    print(array.pop_stack2())
    print(array.pop_stack2())
    print(array.pop_stack2())
    array.print_list()

