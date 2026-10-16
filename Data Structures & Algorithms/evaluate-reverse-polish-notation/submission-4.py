class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for i in tokens:
            if i == "+":
                stk.append(stk.pop()+stk.pop())
            elif i == "-":
                b = stk.pop()
                a = stk.pop()
                stk.append(a-b)
            elif i == "*":
                stk.append(stk.pop()*stk.pop())
            elif i == "/":
                b = stk.pop()
                a = stk.pop()
                stk.append(int(a/b))
            else:
                stk.append(int(i))
        return stk[-1]