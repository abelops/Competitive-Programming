class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pref = [0] * (len(nums)+1)
        
        for start,end in requests:
            pref[start] += 1
            pref[end+1] -= 1
        
        pref = pref[:len(nums)]
        
        for i in range(1,len(pref)):
            pref[i] += pref[i-1]
        
        nums = sorted(nums)
        pref = sorted(pref)
        
        
        ans = 0
        for i in range(len(nums)):
            ans+= nums[i] * pref[i]
            
        return ans % (10**9+7)
        