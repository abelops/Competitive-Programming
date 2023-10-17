class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        l = len(nums)
        mp = {}
        def dp(i, even):
            if i == l:
                return 0
            if (i,even) in mp:
                return mp[(i,even)]
            tot = 0
            if even:
                tot+=nums[i]
            else:
                tot-=nums[i]
            mp[(i,even)] = max(tot+dp(i+1, not even), dp(i+1, even))
            
            return mp[(i,even)]
        return dp(0, True)