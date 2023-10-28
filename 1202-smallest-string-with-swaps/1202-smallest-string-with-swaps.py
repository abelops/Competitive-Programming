class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        rep = {x:x for x in range(len(s))}
        size = [1] * len(s)
        mp = {x: [s[x]] for x in range(len(s))}
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
                mp[repx].extend(mp[repy])
            else:
                rep[repx] = repy
                size[repy] += size[repx]
                mp[repy].extend(mp[repx])
        for i, j in pairs:
            union(i,j)
            
        ans = ""
        for i in range(len(s)):
            heapify(mp[i])
        # print(mp)
        for i in range(len(s)):
            poped = heappop(mp[find(i)])
            ans+=poped
        return ans
                