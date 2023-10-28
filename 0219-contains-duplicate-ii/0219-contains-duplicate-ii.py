class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        for i, n in enumerate(nums):
            if n in mp and abs(i-mp[n]) <= k:
                return True
            mp[n]=i
        return False