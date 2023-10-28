class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowOneCount = list(map(lambda a: 0, range(len(grid[0]))))
        colOneCount = list(map(lambda a: 0, range(len(grid))))
        
        for i in range(len(colOneCount)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rowOneCount[j]+=1
                    colOneCount[i]+=1
        ans = []
        
        
        for i in range(len(grid)):
            r = []
            for j in range(len(grid[i])):
                zerRow = len(rowOneCount) - rowOneCount[j]
                zerCol = len(colOneCount) - colOneCount[i]
                r.append(rowOneCount[j]+colOneCount[i] - zerRow - zerCol )
                
            ans.append(r)
        
        return ans
            