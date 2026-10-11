class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'(':')', '{':'}', '[':']'}
        stk = []
        for i in range(len(s)):
            if s[i] in valid.keys():
                stk.append(s[i])
            if s[i] in valid.values():
                if not stk:
                    return False
                check = stk.pop()
                if valid[check] != s[i]:
                    return False
        if not stk:
            return True
        return False
        
                