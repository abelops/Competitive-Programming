class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        i=l-1
        maxP = 0
        while i-2>=0:
            if(nums[i-2]+nums[i-1]>nums[i]):
                maxP=max(maxP, nums[i-2]+nums[i-1]+nums[i])
            i-=1
        return maxP
        