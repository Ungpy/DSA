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

def infixToPostfix(expression):
    stack1 = ArrayStack() #ใส่ +-*/
    result = ""
    for x in expression:
        if x not in ["+", "-", "*", "/"]:
            result = result + x
        else:
            if stack1.size() > 0:
                if (x in ["+", "-"]) and (stack1.stackTop() in ["*", "/", "+", "-"]):
                    for _ in range(stack1.size()):
                        result = result + stack1.pop()
                if (x in ["*", "/"]) and (stack1.stackTop() in ["*", "/"]):
                    #for _ in range(stack1.size()):
                    result = result + stack1.pop()
            stack1.push(x)
    if not stack1.is_empty():
        for _ in range(stack1.size()):
            result = result + stack1.pop()
    return result

print(infixToPostfix("A+B*C/D-E+F*G"))