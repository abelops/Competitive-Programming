class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        for i in range(1,len(nums)):
            if target > nums[i-1] and target <nums[i]:
                return i
        if nums[-1] > target:
            return 0
        return len(nums)
        