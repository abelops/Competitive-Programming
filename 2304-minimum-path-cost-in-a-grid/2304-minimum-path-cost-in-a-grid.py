class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        r,c = len(grid), len(grid[0])
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1,-1,-1):
                if i < r-1:
                    curSum = [ grid[i+1][x]+moveCost[grid[i][j]][x] for x in range(c)]
                    grid[i][j] += min(curSum)
        return min(grid[0])