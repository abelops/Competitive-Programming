class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i + 1 < len(nums):
                if nums[i] == nums[i+1]:
                    nums[i] = nums[i] * 2
                    nums[i+1] = 0
        ans = []
        z = []
        for i in nums:
            if i != 0:
                ans.append(i)
            else:
                z.append(0)
        ans += z
        return ans