class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        ans = (max(nums) - min(nums)) - (2*k)
        return  ans if ans > 0 else 0 