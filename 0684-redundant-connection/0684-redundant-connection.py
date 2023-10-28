class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = {i:i for i in range(len(edges))}
        size = [1] * len(edges)
        def representative(x):
            if rep[x] == x:
                return x
            rep[x] = representative(rep[x])
            return rep[x]
        def union(x, y):
            xrep = representative(x)
            yrep = representative(y)
            if xrep == yrep:
                return [x,y]
            if size[xrep] > size[yrep]:
                rep[yrep] = rep[xrep]
                size[xrep]+=size[yrep]
            else:
                rep[xrep] = rep[yrep]
                size[yrep]+=size[xrep]
            return None
        for i, j in edges:
            ans = union(i-1, j-1)
            if ans:
                x, y = ans
                return [x+1, y+1]