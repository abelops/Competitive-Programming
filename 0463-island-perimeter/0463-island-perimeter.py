class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        ans = 0
        def dfs(row, col):
            nonlocal visited, ans
            visited[row][col] = True
            for rx, cx in directions:
                newRow = row + rx
                newCol = col + cx
                if inbound(newRow, newCol) and not visited[newRow][newCol] and grid[newRow][newCol]==1:
                    dfs(newRow, newCol)
                elif not inbound(newRow, newCol) or not visited[newRow][newCol]:
                    # print(row,col)
                    ans += 1
        flag = False
        for row in range(len(grid)):
            if flag:
                break
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(row, col)
                    flag = True
                    break
        # print(visited)  
        return ans