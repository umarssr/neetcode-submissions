from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        i,j,longest = 0,0,0
        while j<len(s):
            count[s[j]] +=1
            while sum(count.values())-max(count.values()) >k:
                count[s[i]] -=1
                i+=1
            longest = max(longest, j-i+1)
            j+=1

        return longest