class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maxi = max(counts.values())
        maxDeg = set([x for x in counts if counts[x] == maxi])
        mp = {}
        ans = float("inf")
        for i in range(len(nums)):
            if nums[i] in maxDeg:
                if nums[i] not in mp:
                    mp[nums[i]] = i
        
        for j in range(len(nums)-1,-1,-1):
            if nums[j] in mp:
                ans = min(ans, abs(j - mp[nums[j]] + 1))
                mp.pop(nums[j])
        return ans
        
            
            
        
        