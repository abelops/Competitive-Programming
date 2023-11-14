class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        row, col = len(grid), len(grid[0])
        def inBound(x,y):
            return 0 <= x < row and 0 <= y < col
        def dfs(i,j, visited):
            if not inBound(i,j):
                return 1
            if grid[i][j] == 0:
                return 1
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            ans = 0
            for x, y in d:
                dx = i + x
                dy = j + y
                ans+=dfs(dx, dy, visited)
            return ans
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return dfs(i,j, set())
                        
                
                    
                