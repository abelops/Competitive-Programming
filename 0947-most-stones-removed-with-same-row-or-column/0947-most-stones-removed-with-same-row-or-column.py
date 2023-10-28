class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rep = {i:i for i in range(len(stones))}
        size = [1] * len(stones)
        
        def find(x):
            if x == rep[x]:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x,y):
            repx = find(x)
            repy = find(y)
            
            if repx == repy:
                return
            if size[repx] > size[repy]:
                rep[repy] = repx
                size[repx] += size[repy]
            else:
                rep[repx] = repy
                size[repy]+=size[repx]
        
        for i in range(len(stones)):
            for j in range(i,len(stones)):
                x,y = stones[i] 
                a,b = stones[j]
                if x == a  or y == b:
                    union(i, j)
        ans = 0
        for key, val in rep.items():
            if key == val:
                ans+=size[key] - 1
        return ans 
    