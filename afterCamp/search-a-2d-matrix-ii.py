class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                l, r = 0, len(matrix[0])
                while l < r:
                    mid = l + (r-l)//2
                    if matrix[i][mid] > target:
                        r = mid
                    elif matrix[i][mid] < target:
                        l = mid + 1
                    else:
                        return True
        return False