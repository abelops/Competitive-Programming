class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirc = [(0,1), (0,-1), (1,0), (-1,0)]
        maxArea = 0
        visitedBig = set()
        def isValid(x,y):
            return True if (0 <= x < len(grid) and 0 <= y < len(grid[0])) else False 
            
        def dfs(visited, x, y, area):
            visited.append(tuple([x,y]))
            visitedBig.add(tuple([x,y]))
            for i in dirc:
                dx = x + i[0]
                dy = y + i[1]
                tot = 0
                if isValid(dx, dy) and grid[dx][dy]=="1" and tuple([dx,dy]) not in visited:
                    # print(dx,dy)
                    area=dfs(visited, dx, dy, area+1)
            return area
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and tuple([i,j]) not in visitedBig:
                    calc = dfs([], i,j,1)
                    ans +=1
                    visitedBig.add(tuple([i,j]))
                
        # print(dfs([],6, 7, 1))
        return ans
            
            