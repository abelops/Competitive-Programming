class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        z=0
        ma=0
        l,r=0,1
        if(nums[r]==0):
            z+=1
        if(nums[l]==0):
            z+=1
        while(r<len(nums)):
            if(z<=1):
                ma = max(ma, r-l)
                r+=1
                if(r<len(nums)):
                    if(nums[r]==0):
                        z+=1
            else:
                while(z>1 and l<len(nums)):
                    if(nums[l]==0):
                        z-=1
                    l+=1  
        return ma
            