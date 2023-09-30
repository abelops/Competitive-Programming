class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
                    
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] != -1:
                    if i == 0 and j > 0 and obstacleGrid[i][j-1] == -1:
                        obstacleGrid[i][j] = -1
                    elif i == 0:
                        obstacleGrid[i][j] = 1
                    if j == 0 and i > 0 and obstacleGrid[i-1][j] == -1:
                        obstacleGrid[i][j] = -1
                    elif j == 0:
                        obstacleGrid[i][j] = 1
                if i > 0 and j > 0 and obstacleGrid[i][j] != -1:
                    top = obstacleGrid[i-1][j] if obstacleGrid[i-1][j] != -1 else 0
                    left = obstacleGrid[i][j-1] if obstacleGrid[i][j-1] != -1 else 0
                    obstacleGrid[i][j] = top+left
        # print(obstacleGrid)
        return obstacleGrid[-1][-1] if obstacleGrid[-1][-1] > 0 else 0
    
    