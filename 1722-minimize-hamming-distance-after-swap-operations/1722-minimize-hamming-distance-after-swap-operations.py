class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        leng = len(source)
        rep = {x:x for x in range(leng)}
        size = {x:1 for x in range(leng)}
        
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
                
        for i, j in allowedSwaps:
            union(i,j)
        mp = defaultdict(lambda : Counter())
        for i in range(leng):
            par = find(i)
            mp[par][source[i]]+=1
            mp[par][target[i]]-=1
        # print(mp)
        ans = 0
        for j in range(leng):
            for f in mp[j].values():
                if f > 0:
                    ans+=f
        # print(parents)
        return ans
        