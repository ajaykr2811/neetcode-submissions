class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cf = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            cf[s[i]] = cf.get(s[i],0)+1
            cf[t[i]] = cf.get(t[i],0)-1
            if cf.get(s[i],0) == 0:
                cf.pop(s[i],0)
            if cf.get(t[i],0) == 0:
                cf.pop(t[i],0)
        return cf == {}