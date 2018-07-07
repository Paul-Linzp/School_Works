class Stack: 
    def __init__(self): 
        self.items = [] 

    def isEmpty(self): 
        return len(self.items)==0  

    def push(self, item): 
        self.items.append(item) 

    def pop(self): 
        if not self.isEmpty():
            return self.items.pop()
        return 

    def peek(self): 
        if not self.isEmpty(): 
            return self.items[-1]

    def disp(self):
        if not self.isEmpty():
            return self.items 

    def size(self): 
        return len(self.items) 

if __name__ == "__main__":
    test = Stack()
    print(test.isEmpty())
    test.push(1)
    test.push(2)
    test.push("abc")
    test.push("efg")
    test.push([1, 2])
    test.push([3, 4])
    print(test.disp())
    print(test.size())
    print(test.peek())
    print(test.pop())
    print(test.peek())
    print(test.pop())
    print(test.size())
    print(test.disp())
    