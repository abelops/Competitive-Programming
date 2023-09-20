class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        mp = {chr(x+65):x+1 for x in range(26)}
        tot = 0
        l = len(columnTitle)
        for i in range(l):
            tot+=26**(l-i-1) * mp[columnTitle[i]]
        return tot
            
            