class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mp = {0:1}
        ans = 0
        runningSum = 0
        for i in nums:
            runningSum += i
            if (runningSum - goal) in mp:
                ans+=mp[runningSum - goal]
            mp[runningSum] = 1 + mp.get(runningSum, 0)
        return ans