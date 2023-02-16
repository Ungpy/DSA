class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def push(self, input_data):
        self.data.append(input_data)
        return self.data

    def pop(self):
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            x = self.data.pop()
            return x

    def stackTop(self):
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            return self.data[-1]
    
    def printStack(self):
        print(self.data)

def copyStack(stack1, stack2):
    tempStack = ArrayStack()
    for x in range(stack1.size()):
        top = stack1.pop()
        tempStack.push(top)
    for x in range(stack2.size()):
        stack2.pop()
    for x in range(tempStack.size()):
        top = tempStack.pop()
        stack1.push(top)
        stack2.push(top)



s1 = ArrayStack(); s1.push(10); s1.push(20); s1.push(30)
s2 = ArrayStack(); s2.push(15)
copyStack(s1, s2)
s1.printStack()
s2.printStack()
