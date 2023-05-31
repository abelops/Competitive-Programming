class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        mat = [[0 for i in range(c)] for k in range(r)]
        mat[0][0] = 1
        d = [(-1,0), (0,-1)]
        if obstacleGrid[0][0]:
            return 0
        def inBound(i,j):
            return 0 <= i < r and 0 <= j < c
        
        for i in range(r):
            for j in range(c):
                if not obstacleGrid[i][j]:
                    for x, y in d:
                        dx = i + x
                        dy = j + y
                        if inBound(dx, dy):
                            # print(dx, dy, i, j, r, c, mat)
                            mat[i][j]+= mat[dx][dy]
        return mat[r-1][c-1]
                            