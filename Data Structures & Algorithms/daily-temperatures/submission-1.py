class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stk and stk[-1][1] < t:
                temp_i, temp_t = stk.pop()
                res[temp_i] = i - temp_i
            stk.append((i,t))
        return res

        