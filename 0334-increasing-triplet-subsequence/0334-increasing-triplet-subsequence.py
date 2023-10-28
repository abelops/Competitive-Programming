class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = nums[0]
        min2 = float("inf")
        
        for i in range(1,len(nums)):
            if min2 == float("inf") and nums[i] > min1:
                min2 = nums[i]
            elif nums[i] < min1:
                min1 = nums[i]
            elif nums[i] > min1 and nums[i] > min2:
                return True
            elif nums[i] > min1 and nums[i] < min2:
                min2 = nums[i]
        return False
            