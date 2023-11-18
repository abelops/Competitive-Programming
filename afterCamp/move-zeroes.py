class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l, r = 0, 1
        leng = len(nums)
        while r < len(nums):
            while nums[l] == 0 and r < leng:
                if nums[r] != 0:
                    nums[l], nums[r] = nums[r], nums[l]
                    break
                r+=1
            l+=1
            r+=1
        return nums
            
                