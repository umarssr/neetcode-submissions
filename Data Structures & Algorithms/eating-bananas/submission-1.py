import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            middle = (l+r)//2
            temph=0
            for i in range(len(piles)):
                temph += math.ceil(piles[i]/middle)

            if temph > h:
                l = middle + 1
            else:
                r = middle -1
        return l

            