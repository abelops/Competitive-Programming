class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = 0
        maxP = float("-inf")
        s = 0
        while r < len(nums):
            s+=nums[r]
            if r-l == k-1:
                maxP = max(maxP, s/k)
                s-=nums[l]
                l+=1
            r+=1
        return maxP
            