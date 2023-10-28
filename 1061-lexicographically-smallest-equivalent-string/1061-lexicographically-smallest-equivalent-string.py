class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = {}
        for i, j in zip(s1,s2):
            rep[i] = i
            rep[j] = j
        
        def representative(x):
            if x not in rep:
                return x
            if x == rep[x]:
                return x
            rep[x] = representative(rep[x])
            return rep[x]
        
        def union(x, y):
            xrep = representative(x)
            yrep = representative(y)
            if xrep == yrep:
                return
            if xrep < yrep:
                rep[yrep] = xrep
            elif xrep > yrep:
                rep[xrep] = yrep
            
            
        for i in range(len(s2)):
            union(s2[i], s1[i])
        return "".join([representative(x) for x in baseStr])
            