class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        matrix.append([0] * len(matrix))
        leng = len(matrix)
        def inBound(i,j):
            return 0 <= i < leng and 0 <= j < leng-1
    
        d = [(1,-1), (1, 0), (1, 1)]
        for i in range(leng-2, -1, -1):
            for j in range(leng-1):
                minn = float(inf)
                for x, y in d:
                    dx, dy = i + x, j + y
                    if inBound(dx, dy):
                        minn = min(minn, matrix[dx][dy])
                matrix[i][j]+=minn
        # print(matrix, leng)
        return min(matrix[0])