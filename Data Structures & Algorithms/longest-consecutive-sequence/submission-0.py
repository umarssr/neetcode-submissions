class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        newnums = set(nums)
        starts = []
        for i in nums:
            if i-1 in newnums:
                continue
            else:
                starts.append(i)
        print(starts)
        longest = 1
        for j in starts:
            local = 1
            while j+1 in newnums:
                local +=1
                j+=1
            longest = max(local, longest)
        return longest
                