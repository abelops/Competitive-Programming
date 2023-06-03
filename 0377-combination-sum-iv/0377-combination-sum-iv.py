class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def dp(x, memo):
            if x == target:
                return 1
            if x > target:
                return 0
            if x in memo:
                return memo[x]
            tot = 0
            for i in nums:
                tot += dp(x+i, memo)
            memo[x] = tot
            return tot
        return dp(0, {})