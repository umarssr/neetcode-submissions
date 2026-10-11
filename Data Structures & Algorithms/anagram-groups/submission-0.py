class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)
        for i, word in enumerate(strs):
            temp = word
            charlist = list(temp)
            mydict[tuple(sorted(charlist))].append(word)
        return list(mydict.values())
        
