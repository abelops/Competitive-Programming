class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2
        ans = 0
        l = len(stones)
        @cache
        def dp(cur, i):
            nonlocal ans
            if cur <= target:
                ans = max(ans, cur)
            if i >= l:
                return
            dp(cur+stones[i], i+1)
            dp(cur, i+1)
        
        for i in range(l):
            dp(0, i)
        return abs(sum(stones) - (2*ans))
