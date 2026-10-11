class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}
        for i in s1:
            if i not in counts1:
                counts1[i] = 1
            else:
                counts1[i] +=1
        window_length = len(s1)
        i = 0
        j = i+window_length

        while j <= len(s2):
            counts2 = {}
            for char in s2[i:j]:
                if char not in counts2:
                    counts2[char] = 1
                else:
                    counts2[char] +=1
            if counts1 == counts2:
                return True
            i+=1
            j+=1
        return False