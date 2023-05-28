class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        dest = len(cost)
        ans = float("inf")
        def recur(n):
            if n >= dest:
                return 0
            if n in memo:
                return memo[n]
            memo[n] = min(recur(n+1) + cost[n], recur(n+2) + cost[n])
            return memo[n]      
        return min(recur(0), recur(1))