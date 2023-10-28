class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l,r=0,0
        m=1
        ans = 0
        while r<len(nums):
            m*=nums[r]
            while (m>=k and l<len(nums)):
                m=int(m/nums[l])
                l+=1
            ans+=r-l+1
            r+=1
            if(ans<0):
                ans=0
        return ans