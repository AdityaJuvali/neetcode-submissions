class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        if len(s) != len(t):
            return False
        else:
            for i in s:
                d1[i]=0
            for i in t:    
                d2[i]=0
            for i in range(len(s)):
                d1[s[i]] = d1[s[i]] + 1
                d2[t[i]] = d2[t[i]] + 1
            if d1 != d2:
                return False
        return True