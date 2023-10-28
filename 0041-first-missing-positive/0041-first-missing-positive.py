class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nLen = len(nums) + 1
        for i, n in enumerate(nums):
            while 0 < n < nLen and nums[n-1] != n:
                nums[i], nums[n-1] = nums[n-1], n
                n = nums[i]
        for i, n in enumerate(nums):
            if i+1 != n:
                return i+1
        return nLen
            