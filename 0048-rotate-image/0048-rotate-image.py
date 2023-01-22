from math import ceil
class Solution:
    def transpose(self, mat):
        for i in range(len(mat)):
            for j in range(i,len(mat[i])):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        return mat
    
    def rev(self, mat):
        for i in range(len(mat)):
            l,r = 0, len(mat[0])-1
            while l < r:
                mat[i][l], mat[i][r] = mat[i][r], mat[i][l]
                l+=1
                r-=1
        return mat
            
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.rev(self.transpose(matrix))
                
                
                
        