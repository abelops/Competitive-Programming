class Solution:
    def getThreeByThree(self, i, j, grid):
        ma = 0
        for i1 in range(i, i+3):
            for j1 in range(j, j+3):
                if grid[i1][j1] > ma:
                    ma = grid[i1][j1]
        return ma
        
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ansList = [[] for x in range(len(grid)-2)]
        
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i+2 < len(grid) and j+2 < len(grid):
                    ma = self.getThreeByThree(i, j, grid)
                    ansList[i].append(ma)
        
        return ansList
        