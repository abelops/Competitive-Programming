class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        leng = len(triangle)
        for i in range(leng-2, -1, -1):
            for j in range(i+1):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]