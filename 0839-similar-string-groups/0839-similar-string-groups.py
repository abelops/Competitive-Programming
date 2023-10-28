class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        rep = {}
        for word in strs:
            rep[word] = word
        
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
        
        for i, word in enumerate(strs):
            for j in range(i,len(strs)):
                diff = [char1 for char1, char2 in zip(word, strs[j]) if char1 != char2]
                if len(diff) <= 2:
                    union(word, strs[j])
        ans = set()
        for word in strs:
            par = representative(word)
            ans.add(par)
        return len(ans)
                