class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myset = []
        for i, number in enumerate(nums):
            looking_for = target - number
            if looking_for in myset:
                return [nums.index(looking_for), i]
            else:
                myset.append(nums[i])

            