class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = list(s)
        s2 = list(t)
        if len(s1)!=len(s2):
            return False
        s1.sort()
        s2.sort()
        if(s1==s2):
            return True
        return False