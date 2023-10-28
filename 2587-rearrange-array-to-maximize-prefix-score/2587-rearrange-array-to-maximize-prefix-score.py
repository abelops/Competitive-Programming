class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums = sorted(nums)[::-1]
        pref = 0
        ans = 0
        for num in nums:
            pref+=num
            if pref > 0:
                ans+=1
        return ans
        
        