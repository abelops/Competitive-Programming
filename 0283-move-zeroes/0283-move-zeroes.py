class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)
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
                l+=1
                r+=1
            else:
                l+=1
                
        
