class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[1 for x in range(n)] for x in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                mat[i][j] = mat[i-1][j] + mat[i][j-1]           
        return mat[m-1][n-1]
                                    