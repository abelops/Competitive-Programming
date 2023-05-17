class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        rep = {(i,j):(i,j) for i in range(n) for j in range(m)}
        size = {(i,j):1 for i in range(n) for j in range(m)}
        d = {
            1: set([(0,1),(0,-1,)]),
            2: set([(1,0),(-1,0)]),
            3: set([(0,-1),(1,0)]),
            4: set([(0,1),(1,0)]),
            5: set([(-1,0),(0,-1)]),
            6: set([(-1,0),(0,1)])
        }
        def inBound(x,y):
            return 0 <= x < n and 0 <= y < m
        def representative(x):
            if rep[x] == x:
                return x
            rep[x] = representative(rep[x])
            return rep[x]
        
        def union(x, y):
            xrep = representative(x)
            yrep = representative(y)
            if xrep == yrep:
                return
            if size[xrep] > size[yrep]:
                rep[yrep] = rep[xrep]
                size[xrep]+=size[yrep]
            else:
                rep[xrep] = rep[yrep]
                size[yrep]+=size[xrep]
        
        for i in range(n):
            for j in range(m):
                pos = grid[i][j]
                for x,y in d[pos]:
                    dx = i + x
                    dy = j + y
                    if inBound(dx, dy):
                        new = grid[dx][dy]
                        if (-x, -y) in d[new]:
                            union((dx,dy), (i,j))
        return representative((0,0)) == representative((n-1,m-1))
                        
                
        