class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        c = 0
        d = [(1,0),(0,1)]
        
        def isValid(i,j):
            return 0 <= i < m and 0 <= j < n
        memo = {}
        def dfs(i, j):
            if (i, j) == (m-1, n-1):
                return 1
            temp = 0
            for x, y in d:
                dx = i + x
                dy = j + y
                if isValid(dx, dy):
                    if (dx, dy) in memo:
                        temp+=memo[(dx,dy)]
                    else:
                        temp += dfs(dx, dy)
            memo[(i,j)] = temp
            return temp
        return dfs(0,0)
        # print(memo)
        # return /c