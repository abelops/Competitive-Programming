class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        if len(nums)==1:
            return nums[0]
        for i in nums:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]=mp[i]+1
                if mp[i]>len(nums)/2:
                    return i