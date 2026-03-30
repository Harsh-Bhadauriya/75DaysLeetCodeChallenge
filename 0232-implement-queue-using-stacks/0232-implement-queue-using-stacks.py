class MyQueue:

    def __init__(self):
        self.i, self.o = [], []

    def push(self, x):
        self.i.append(x)

    def pop(self):
        if not self.o:
            self.o = self.i[::-1]
            self.i = []
        return self.o.pop()

    def peek(self):
        if not self.o:
            self.o = self.i[::-1]
            self.i = []
        return self.o[-1]

    def empty(self):
        return not self.i and not self.o