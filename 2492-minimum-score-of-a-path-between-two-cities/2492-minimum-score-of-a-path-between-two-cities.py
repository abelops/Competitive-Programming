class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rep = {i:i for i in range(n)}
        size = [1] * n
        mp = defaultdict(int)
        
        def find(x):
            if x == rep[x]:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x, y):
            xrep = find(x)
            yrep = find(y)
            
            if xrep == yrep:
                return
            if size[xrep] > size[yrep]:
                rep[yrep] = xrep
                size[xrep]+=size[yrep]
            else:
                rep[xrep] = yrep
                size[yrep]+=size[xrep]
            return
        minn = float("inf")
        for i,j,d in roads:
            union(i-1, j-1)
            
        for i,j,d in roads:
            if find(i-1) == find(0):
                minn = min(minn, d)
        return minn
        
        
        