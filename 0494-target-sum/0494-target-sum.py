class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tot = len(nums)
        memo = defaultdict(int)
        def dp(n, cur):
            if cur == tot and n == target:
                return 1
            if (n, cur) in memo:
                return memo[(n,cur)]
            if cur < tot:
                memo[(n, cur)] += dp(n+nums[cur], cur+1)
                memo[(n, cur)] += dp(n-nums[cur], cur+1)
            return memo[(n,cur)]
        return dp(0,0)