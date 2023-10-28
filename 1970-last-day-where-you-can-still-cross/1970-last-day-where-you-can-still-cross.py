class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        rep = {(x,y):(x,y) for x in range(row) for y in range(col)}
        size = {(x,y):1 for x in range(row) for y in range(col)}
        d = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]
        visited = set()
        
        def find(x):
            if x == rep[x]:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x, y):
            repx = find(x)
            repy = find(y)
            
            if repx == repy:
                return
            if size[repx] > size[repy]:
                rep[repy] = repx
                size[repx] += size[repy]
            else:
                rep[repx] = repy
                size[repy] += size[repx]
        rep[0] = 0
        rep[-1] = -1
        size[0] = 1
        size[-1] = 1
        
        count = 0
        for i, j in cells:
            i-=1
            j-=1
            for x, y in d:
                dx = x + i 
                dy = y + j
                
                if 0 <= dx < row:
                    if 0 <= dy < col:
                        if (dx, dy) in visited:
                            union((dx, dy), (i, j))
                    else:
                        if dy == -1:
                            union((i,j), 0)
                        elif dy == col:
                            union((i, j), -1)
                if find(0) == find(-1):
                    return count
                visited.add((i,j))
            count+=1
                
        return col
                    
                
        