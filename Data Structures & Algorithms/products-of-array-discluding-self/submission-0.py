class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i] * 1)
            else:
                prefix.append(nums[i] * prefix[-1])
        postfix = []
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix.append(nums[i])
            else:
                postfix.append(nums[i] * postfix[-1])
        postfix.reverse()
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[i+1])
            elif i == len(nums)-1:
                res.append(prefix[i-1])
            else:
                res.append(postfix[i+1]*prefix[i-1])
        return res
