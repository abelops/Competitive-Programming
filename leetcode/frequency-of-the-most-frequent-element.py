class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:	
        nums.sort()
        l, r = 0, 0
        tot, res = 0, 0
        while (r < len(nums)):
            tot += nums[r]
            
            while nums[r]*(r-l+1) > tot+k:
                tot -= nums[l]
                l+=1
            res = max(res, r-l+1)
            r+=1
        return res