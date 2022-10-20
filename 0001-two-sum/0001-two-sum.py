class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i,n in enumerate(nums):
            if target-n not in mp:
                mp[n]=i
            else:
                return [i, mp[target-n]]