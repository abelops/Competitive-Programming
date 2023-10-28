class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            ind = nums[i] - 1
            if nums[i] == nums[ind] and ind != i:
                return nums[i]
            if ind != i:
                nums[i], nums[ind] = nums[ind], nums[i]
            else:
                i+=1
        print(nums)
        return ans
                