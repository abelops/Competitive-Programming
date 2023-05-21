class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        rep = {x:x for x in range(len(points))}
        size = {x:1 for x in range(len(points))}
        
        def find(x):
            if x == rep[x]:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x, y):
            repx = find(x)
            repy = find(y)
            if repx == repy:
                return 
            if size[repx] > size[repy]:
                rep[repy] = repx
                size[repx]+=size[repy]
            else:
                rep[repx] = repy
                size[repy]+=size[repx]
        ans = []
        for i in range(len(points)):
            for j in range(i, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                ans.append([dist, i, j])
        ans.sort()
        tot = 0
        for dist, i, j in ans:
            if find(i) != find(j):
                union(i, j)
                tot += dist
        return tot