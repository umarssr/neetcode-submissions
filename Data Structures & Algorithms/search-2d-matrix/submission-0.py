class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        total = []
        for i in matrix:
            total +=i
        l,r = 0, len(total)-1
        while l<=r:
            m = (l+r)//2
            if total[m] == target:
                return True
            elif total[m] > target:
                r = m-1
            else:
                l=m+1
        return False
            