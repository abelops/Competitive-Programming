class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recur(n):
            if n < 2:
                return 1
            if n in memo:
                return memo[n]
            memo[n-1] = recur(n-1)
            memo[n-2] = recur(n-2)
            return memo[n-1] + memo[n-2]
        return recur(n)
            