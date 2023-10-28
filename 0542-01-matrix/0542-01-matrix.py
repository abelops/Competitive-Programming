class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        m, n = len(mat), len(mat[0])
        def checkValid(x,y):
            return 0 <= x < m and 0 <= y < n   
        
        q = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        while q:
            level = 0
            while q:
                l = len(q)
                for i in range(l):
                    x, y = q.popleft()
                    if mat[x][y] == 1:
                        mat[x][y] = level
                    for a, b in d:
                        dx, dy = (x + a, y + b)
                        if checkValid(dx, dy) and (dx,dy) not in visited and mat[dx][dy]:
                            q.append((dx, dy))
                            visited.add((dx, dy))
                level+=1
        return mat
                          