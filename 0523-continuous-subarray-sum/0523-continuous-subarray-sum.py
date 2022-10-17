class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pref = 0
        mp = {0:-1}
        for i,n in enumerate(nums):
            pref+=nums[i]
            rem = pref % k
            if rem not in mp:
                mp[rem]=i
            elif i-mp[rem]>1:
                return True
        return False