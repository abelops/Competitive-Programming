class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = sorted(nums)
        return n == nums or n[::-1] == nums