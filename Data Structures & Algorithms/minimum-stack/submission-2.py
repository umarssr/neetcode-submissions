class MinStack:

    def __init__(self):
        self.stk = []
        self.minimum = []
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.minimum:
            current_min = self.minimum[-1]
        else:
            current_min = float('inf')
        if val < current_min:
            self.minimum.append(val)
        else:
            self.minimum.append(current_min)
    def pop(self) -> None:
        
        self.stk.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stk[-1]
        
    def getMin(self) -> int:
        return self.minimum[-1]
        
