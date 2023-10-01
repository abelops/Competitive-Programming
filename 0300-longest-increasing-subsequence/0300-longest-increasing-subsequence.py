class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        memo = {}
        def dfs(cur):
            if cur in memo:
                return memo[cur]
            tot = 1
            for i in range(cur+1, l):
                if nums[i] > nums[cur]:
                    tot = max(tot, dfs(i)+1)
            memo[cur] = tot   
            return tot
        
        ans = 0
        for i in range(l):
            ans = max(ans, dfs(i))
        return ans
                            
            
            