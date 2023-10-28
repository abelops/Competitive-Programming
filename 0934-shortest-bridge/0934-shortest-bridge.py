class Solution:
    def shortestBridge(self, mat: List[List[int]]) -> int:
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        m = n = len(mat)
        def checkValid(x,y):
            return 0 <= x < m and 0 <= y < n   
        
        def dfs(i, j, visited):
            visited.add((i,j))
            for x, y in d:
                dx = i + x
                dy = j + y
                if checkValid(dx, dy) and mat[dx][dy] == 1 and (dx, dy) not in visited:
                    dfs(dx, dy, visited)   
            return visited        
        
        def bfs(q):
            level = 0
            visited = q
            q = deque(q)
            while q:
                qlen = len(q)
                stat = False
                for _ in range(qlen):
                    popedX, popedY = q.popleft()
                    for x, y in d:
                        dx = popedX + x
                        dy = popedY + y
                        if checkValid(dx, dy) and (dx, dy) not in visited:
                            q.append((dx,dy))
                            if mat[dx][dy] == 1:
                                return level
                            visited.add((dx,dy))
                level+=1
               
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    q = dfs(i,j, set())
                    return bfs(q)
            