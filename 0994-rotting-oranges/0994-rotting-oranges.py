class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def check(cur):
            return 0 <= cur[0] <len(grid) and 0 <= cur[1] <len(grid[0])
        
        d = [(1,0), (-1,0), (0,1), (0,-1)]
        q = deque()
        spoiled = set()
        toVisit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                    spoiled.add((i,j))
                if grid[i][j] == 1 or grid[i][j] == 2:
                    toVisit.add((i,j))
        t = 0  
        # print(spoiled, q)
        tot = []
        while q:
            l = len(q)
            temp = []
            for i in range(l):
                poped = q.popleft()
                for i in d:
                    cur = (poped[0]+i[0], poped[1]+i[1])
                    if check(cur) and cur not in spoiled and cur in toVisit:
                        q.append(cur)
                        spoiled.add(cur)
                        temp.append((i,j))
            if temp:
                tot.append(temp)
                t+=1
        # print(spoiled)
        # print(tot)
        if len(spoiled) == len(toVisit):
            return t
        else:
            return -1
            