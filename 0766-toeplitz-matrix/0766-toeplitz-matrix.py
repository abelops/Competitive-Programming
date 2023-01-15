class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ans = {}
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i - j not in ans :
                    ans[i-j] = matrix[i][j]
                elif ans[i-j] != matrix[i][j]:
                    return False
                         
        return True  
        