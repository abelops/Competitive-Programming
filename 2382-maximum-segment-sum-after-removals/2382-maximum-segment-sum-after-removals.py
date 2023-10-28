class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        rep = {x:x for x in range(len(nums))}
        size = {x:0 for x in range(len(nums))}
        val = {x:0 for x in range(len(nums))}
        ans = []
        maxi = 0
        def inRange(x):
            return 0 <= x < len(nums)
        
        def find(x):
            if x == rep[x]:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x, y):
            nonlocal maxi
            repx = find(x)
            repy = find(y)
            
            if repx == repy:
                return
            if size[repx] > size[repy]:
                rep[repy] = repx
                size[repx] += size[repy]
                val[repx] += val[repy]
                # maxi = max(maxi, val[repx])
            else:
                rep[repx] = repy
                size[repy] += size[repx]
                val[repy] += val[repx]
                # maxi = max(maxi, val[repy])
                
                
        for j in range(len(nums)-1, -1, -1):
            i = removeQueries[j]
            ans.append(maxi)
            val[i]+=nums[i]
            if inRange(i+1) and val[i+1] > 0:
                union(i, i+1)
            if inRange(i-1) and val[i-1] > 0:
                union(i, i-1)
            par = find(i)
            maxi = max(maxi, val[par])
        return ans[::-1]
                