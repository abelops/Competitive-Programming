class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = []
        for i in range(len(matrix)):
            pre = [matrix[i][0]]
            for j in range(1,len(matrix[i])):
                pre.append(pre[-1]+matrix[i][j])
            self.mat.append(pre)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1,row2+1):
            if col1>0:
                ans+=self.mat[i][col2]-self.mat[i][col1-1]
            else:
                ans+=self.mat[i][col2]
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)