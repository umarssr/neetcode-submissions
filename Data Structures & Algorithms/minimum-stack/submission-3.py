class MinStack:

    def __init__(self):
        self.stk = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.minimum and self.minimum[-1] > val:
            self.minimum.append(val)
        elif not self.minimum:
            self.minimum.append(val)
        else:
            self.minimum.append(self.minimum[-1])
    
    def pop(self) -> None:
        self.stk.pop()
        self.minimum.pop()  

    def top(self) -> int:
        return self.stk[-1]
        
    def getMin(self) -> int:
        return self.minimum[-1]
        
