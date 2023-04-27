class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        d = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        
        def isValid(i):
            return 0 <= i[0] < len(grid) and 0 <= i[1] < len(grid[0])
        
        if grid[0][0] !=0:
            return -1
        q = deque([[0,0]])
        grid[0][0] = 1
        ans = 0
        while q:
            ans+=1
            l = len(q)
            for i in range(l):
                poped = q.popleft()
                for i in d:
                    cur = [poped[0]+i[0], poped[1]+i[1]]
                    if cur == [len(grid), len(grid)]:
                        return ans
                    if isValid(cur) and grid[cur[0]][cur[1]] == 0:
                        q.append(cur)
                        grid[cur[0]][cur[1]] = 1       
        return -1