class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = []
        for i in range(len(nums)):
            l.append(nums[i]+nums[len(nums)-1-i])
        return max(l)