class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

