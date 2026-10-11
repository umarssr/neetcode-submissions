class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m +1
            else:
                r= m
        print(nums[l], nums)
        brkpt = l
        if brkpt != 0 and target >= nums[0]:
            l = 0
            r = brkpt -1
            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m+1
        else:
            l = brkpt
            r = len(nums) -1
            while l <=r:
                m = (l+r)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m+1
        return -1
