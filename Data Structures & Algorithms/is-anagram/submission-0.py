class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = 26 * [0]
        t_list = 26 * [0]

        for i in s:
            ch  = ord(str(i)) - ord("a")
            print(ch)
            s_list[ch] +=1
            
        for i in t:
            ch  = ord(str(i)) - ord("a")
            t_list[ch] +=1
        if s_list == t_list:
            return True

        return False
                


