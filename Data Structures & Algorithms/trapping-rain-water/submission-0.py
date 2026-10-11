class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = []
        maxr = []
        res = 0
        maxl_counter = 0
        maxr_counter = 0
        for i in height:
            if i > maxl_counter:
                maxl.append(maxl_counter)
                maxl_counter = i
            else:
                maxl.append(maxl_counter)
        for i in reversed(height):
            if i > maxr_counter:
                maxr.append(maxr_counter)
                maxr_counter = i
            else:
                maxr.append(maxr_counter)
        maxr = list(reversed(maxr))
        print(maxl, maxr)
        for i in range(len(height)):
            posa = min(maxl[i], maxr[i])
            res += max(0, posa - height[i])
        return res

