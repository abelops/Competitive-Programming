class Solution:
    def rob(self, nums: List[int]) -> int:
        leng = len(nums)
        if leng < 3:
            return max(nums)
        ans = [0] * leng
        ans[0], ans[1] = nums[0], max(nums[1], nums[0])
        for i in range(2, leng):
            ans[i] = max(ans[i-1], ans[i-2] + nums[i])
        return ans[-1]
            
                
            