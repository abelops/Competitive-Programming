class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        tot = 0
        l = len(columnTitle)
        for i in range(l):
            tot+=26**(l-i-1) * (ord(columnTitle[i]) - 64 )
        return tot
            
            