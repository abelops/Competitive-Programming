class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        arr = [1] * l
        for i in range(l-1, -1, -1):
            cur = 1
            for j in range(i, l):
                if nums[i] < nums[j]:
                    cur = max(cur, arr[j]+1)
            arr[i] = cur
        return max(arr)
