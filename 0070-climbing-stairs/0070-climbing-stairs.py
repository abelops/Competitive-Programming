class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(cur, memo):
            if cur == n:
                return 1
            if cur in memo:
                return memo[cur]
            ans = dp(cur+1, memo)
            if cur + 2 <= n:
                ans += dp(cur+2, memo)
            memo[cur] = ans
            return ans
        return dp(0, {})
    
    