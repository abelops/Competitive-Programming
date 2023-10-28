class Solution:
    def containsDuplicate(self, nums):
        mp = {}
        for i in nums:
            if i in mp:
                return True
            mp[i]=i
        return False