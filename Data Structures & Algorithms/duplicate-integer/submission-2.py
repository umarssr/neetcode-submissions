class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already = set()
        for n in nums:
            if n in already:
                return True
            already.add(n)
        return False