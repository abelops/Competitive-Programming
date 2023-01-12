class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if i == 0 and matrix[i][0] > target:
                return False
            if matrix[i][0] == target:
                return True
            if matrix[i][0] > 0:
                for j in matrix[i-1]:
                    if j == target:
                        return True
            if i == len(matrix) -1:
                for j in matrix[i]:
                    if j == target:
                        return True
        return False
                
                