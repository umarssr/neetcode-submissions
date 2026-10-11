class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        myset= set()
        longest = 0
        while j < len(s):
            if s[j] not in myset:
                myset.add(s[j])
                j+=1
                longest = max(longest, j-i)
            else:
                myset.remove(s[i])
                i+=1
        return longest

