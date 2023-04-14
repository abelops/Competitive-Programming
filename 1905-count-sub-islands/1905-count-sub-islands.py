class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def inBound(i, j):
            return 0 <= i < len(grid2) and 0 <= j < len(grid2[0])
        
        visited = set() 
        stat = True
        def dfs(i, j, ans):
            nonlocal stat
            visited.add((i,j))
            if grid1[i][j] != 1:
                stat = False
            ans.append((i,j))
            for r, c in directions:
                di = i + r
                dj = j + c
                # print(di, dj)
                if inBound(di, dj) and grid2[di][dj] == 1 and (di,dj) not in visited:
                    if grid1[di][dj] != 1:
                        stat = False
                        # print("HEREE")
                    dfs(di, dj, ans)
            return ans if stat else []
        
        c = 0
        # temp = dfs(3,2,[])
        # print(temp)
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i,j) not in visited:
                    stat = True
                    ans = dfs(i,j,[])
                    if ans:
                        c+=1  
        return c
            
                    