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

def is_parentheses_matching(expression):
    myStack = ArrayStack()
    for x in expression:
        if x == "(":
            myStack.push("(")
        elif x == ")":
            if myStack.stackTop() == "(":
                myStack.pop()
            else:
                return False #ถ้าวงเล็บปิดเกินวงเล็บเปิดที่มี
    return myStack.is_empty()

print(is_parentheses_matching("(((A+B)*C)"))