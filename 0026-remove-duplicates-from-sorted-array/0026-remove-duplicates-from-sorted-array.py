class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        1. assign left and right pointer
        2. loop until r<len(nums)
        3. if nums[l]==nums[r]: r+=1
        4. else: l+=1 nums[l]=nums[r]
        5. return l+1
        """
        l=0
        r=0
        while r<len(nums):
            if nums[r]==nums[l]:
                r+=1
            else:
                l+=1
                nums[l]=nums[r]
        return l+1