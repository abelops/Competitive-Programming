class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        window = len(s1)
        totLen = len(s2)
        s1 = sorted(s1)
        while r < totLen:
            if r-l+1 == window:
                win = sorted(s2[l:r+1])
                if win == s1:
                    return True
                l+=1
            else:
                r+=1
        return False