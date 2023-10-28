class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = {}
        le = len(nums)
        if le==1:
            return [nums[0]]
        ans = []
        for i in nums:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]=mp[i]+1
            if mp[i]>le/3:
                ans.append(i)
        return list(set(ans))