class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        ptr1 = 0
        ptr2 = 1
        while ptr1 < len(temperatures):
            if ptr2 >= len(temperatures):
                ptr1 +=1
                ptr2 = ptr1+1
            elif temperatures[ptr2] > temperatures[ptr1]:
                res[ptr1] = ptr2-ptr1
                ptr1+=1
                ptr2 = ptr1+1
            else:
                ptr2+=1
        return res


