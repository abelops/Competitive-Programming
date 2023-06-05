class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sat = sorted(satisfaction)
        leng = len(satisfaction)
        maxi = -float("inf")
        memo = {}
        def dfs(tot, cur, m):
            if cur == leng:
                return tot
            if (cur, m) in memo:
                return memo[(cur, m)]
            memo[(cur, m)] = dfs(tot + (sat[cur] * m), cur+1, m+1) 
            return memo[(cur, m)]
            
        for i in range(leng-1, -1, -1):
            ret = dfs(0, i, 1)
            if ret <= maxi:
                break
            maxi = max(maxi, ret)
        return maxi if maxi > 0 else 0