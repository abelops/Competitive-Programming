class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def inBound(i, j):
            return 0 <= i < len(grid2) and 0 <= j < len(grid2[0])
        
        visited = [[False for x in grid2[0]] for x in grid2]
        stat = True
        def dfs(i, j):
            nonlocal stat, visited
            visited[i][j] = True
            if grid1[i][j] != 1:
                stat = False
            for r, c in directions:
                di = i + r
                dj = j + c
                if inBound(di, dj) and grid2[di][dj] == 1 and not visited[di][dj]:
                    if grid1[di][dj] != 1:
                        stat = False
                    dfs(di, dj)
            return 1 if stat else 0
        
        c = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and not visited[i][j]:
                    stat = True
                    ans = dfs(i,j)
                    if ans:
                        c+=1  
        return c