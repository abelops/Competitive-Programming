class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            mp[i] = nums[i]
        
        ans = []
        
        for i in nums:
            ans.append(mp[i])
            
        return ans