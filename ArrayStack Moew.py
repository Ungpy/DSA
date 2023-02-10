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

myStack= ArrayStack()
myStack.push(10);myStack.push(20); myStack.push(30)
myStack.printStack()
print(myStack.stackTop())
x= myStack.pop()
print(x)
myStack.pop()
myStack.printStack()
myStack.pop()
print(myStack.is_empty())
myStack.pop()