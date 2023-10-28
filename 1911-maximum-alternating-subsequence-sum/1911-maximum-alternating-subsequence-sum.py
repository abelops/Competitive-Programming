class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        ans = max(nums)
        l = len(nums)
        @cache
        def dp(i, even):
            if i == l:
                return 0
            maxi = 0
            left = dp(i+1, even)
            maxi = max(maxi, left)
            if even:
                right = dp(i+1, not even) + nums[i]
                maxi = max(maxi, right)
            else:
                right = dp(i+1, not even) - nums[i]
                maxi = max(maxi, right)
            return maxi
        return dp(0, True)