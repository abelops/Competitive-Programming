class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(max(nums)+1):
            ans = i
            if i not in nums:
                return i
        return i+1