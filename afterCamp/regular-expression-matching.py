class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ilen = len(s)
        jlen = len(p)
        @cache
        def dp(i,j):
            if i >= ilen and j >= jlen:
                return True
            if j >= jlen:
                return False
            
            stat = i < ilen and  (s[i] == p[j] or p[j] == ".")
            if j+1 < jlen:
                if p[j+1] == "*":
                    if stat:
                        left = dp(i+1,j)
                        if left:
                            return True
                    right = dp(i, j+2)
                    if right:
                        return True
            if stat:
                return dp(i+1, j+1)
            return False         
        return dp(0,0)
                
                    