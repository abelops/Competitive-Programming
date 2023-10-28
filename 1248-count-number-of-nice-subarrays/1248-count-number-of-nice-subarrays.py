class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        mp = {0:1}
        runningSum = 0
        ans = 0
        for i in nums:
            runningSum += i
            if runningSum - k in mp:
                ans+=mp[runningSum - k]
            if runningSum not in mp:
                mp[runningSum] = 1
            else:
                mp[runningSum] += 1
        return ans
        
        
            
