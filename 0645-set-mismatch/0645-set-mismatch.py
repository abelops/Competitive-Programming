class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        miss = []
        mp = {}
        mis=0
        for i in range(len(nums)):
            if i+1 not in nums:
                mis = i+1
                miss.append(mis)
            if nums[i] not in mp:
                mp[nums[i]] = i
            else:
                ans.append(nums[i])
                mis=0
        fin = []
        for i in range(len(ans)):
            fin.append(ans[i])
            fin.append(miss[i])
        return fin