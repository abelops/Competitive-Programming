class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        ans = [0] * l
        
        for i in range(l-1,-1,-1):
            if i == l-1:
                ans[i] = 1
                continue
            cur = 1
            for j in range(i+1, l):
                if nums[j] > nums[i]:
                    cur = max(cur, ans[j]+1)
            ans[i] += cur
        return max(ans)
            
            