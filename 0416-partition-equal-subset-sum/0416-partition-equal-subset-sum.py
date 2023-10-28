class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2:
            return False
        
        target = tot//2
        ans = [False] * (target + 1)
        ans[0] = True
        for n in nums:
            for j in range(target, n-1, -1):
                ans[j] |= ans[j-n]
            # print(ans)
        
        return ans[target]
                
                