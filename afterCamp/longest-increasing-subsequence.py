class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # l = len(nums)
        # @cache
        # def dp(i):
        #     if i > l:
        #         return 0
        #     curMax = 1
        #     for j in range(i,l):
        #         if nums[j] > nums[i]:
        #             curMax = max(curMax, dp(j)+1)
        #     return curMax
        # ans = 0
        # for i in range(l):
        #     ans = max(ans, dp(i))
        # return ans
        l = len(nums)
        arr = [0] * l
        ans = 1
        for i in range(l-1,-1,-1):
            maxi = 1
            for j in range(i+1, l):
                if nums[j] > nums[i]:
                    maxi = max(maxi, arr[j]+1 )
            arr[i]+=maxi
            if arr[i] > ans:
                ans = arr[i]
        return ans
        