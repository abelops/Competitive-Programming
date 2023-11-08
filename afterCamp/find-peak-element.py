class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(float("-inf"))
        nums = nums[::-1]
        nums.append(float("-inf"))
        nums = nums[::-1]
        
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                return i-1