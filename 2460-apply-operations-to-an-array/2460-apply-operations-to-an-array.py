class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i + 1 < len(nums):
                if nums[i] == nums[i+1]:
                    nums[i] = nums[i] * 2
                    nums[i+1] = 0
        l = 0
        r = 1
        while r < len(nums):
            if nums[r] == 0:
                r+=1
                continue
            if l == r:
                r+=1
                continue
            if nums[l] == 0:
                nums[l] = nums[r]
                nums[r] = 0
                if l+1 < len(nums):
                    l+=1
                elif r+1 < len(nums):
                    r+=1
            else:
                l+=1
                    
        return nums
