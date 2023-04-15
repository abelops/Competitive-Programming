class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m = max(nums)
        if m <=0:
            return 1
        nums = set(nums)
        for i in range(1, m):
            if i not in nums:
                return i
        return m+1