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