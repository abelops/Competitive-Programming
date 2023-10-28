class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        rep = {x:x for x in range(n)}
        size = {x:1 for x in range(n)}
        
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
                size[repx] += size[repy]
            else:
                rep[repx] = repy
                size[repy] += size[repx]
        ans = []
        for i, j in requests:
            repi = find(i)
            repj = find(j)
            stat = True
            for x, y in restrictions:
                repx = find(x)
                repy = find(y)
                if repi == repx and repj == repy or repj == repx and repi == repy:
                    stat = False
                    break
            if stat:
                union(i, j)
            ans.append(stat)
        return ans
                    
            