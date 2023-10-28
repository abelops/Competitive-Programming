class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if k > l:
            k %= l
        nums[:] = nums[-k:] + nums[:-k]
        