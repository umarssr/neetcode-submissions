class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for char in tokens:
            if char == "+":
                stk.append(stk.pop()+stk.pop())
            elif char == "-":
                b= stk.pop()
                a = stk.pop()
                stk.append(a-b)
            elif char == "*":
                stk.append(stk.pop()*stk.pop())
            elif char == "/":
                b = stk.pop()
                a = stk.pop()
                stk.append(int(a/b))
            else:
                stk.append(int(char))
        return stk[-1]