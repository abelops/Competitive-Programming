class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for i in range(l//2):
            if l % (i+1) == 0:
                st = s[0:i+1] * (l//(i+1)) 
                if st == s:
                    return True
        return False
                