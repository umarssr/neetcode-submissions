class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = "+-*/"
        for i in tokens:
            if i not in ops:
                stk.append(int(i))
            elif i == "+":
                digit2 = stk.pop()
                digit1 = stk.pop()
                stk.append(digit1+digit2)
            elif i == "-":
                digit2 = stk.pop()
                digit1 = stk.pop()
                stk.append(digit1-digit2)
            elif i == "*":
                digit2 = stk.pop()
                digit1 = stk.pop()
                stk.append(digit1*digit2)
            elif i == "/":
                digit2 = stk.pop()
                digit1 = stk.pop()
                stk.append(int(digit1/digit2))
        return stk[-1]