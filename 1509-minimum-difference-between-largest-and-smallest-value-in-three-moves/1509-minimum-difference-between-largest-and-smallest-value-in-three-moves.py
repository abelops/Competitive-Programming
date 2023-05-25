class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        leng = len(nums)
        if leng < 5:
            return 0
        ans = float("inf")
        for i in range(4):
            ans = min(ans, nums[i-4] - nums[i])
            
        return ans
        