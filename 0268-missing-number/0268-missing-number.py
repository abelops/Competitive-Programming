class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [-1]  * (len(nums) +1)
        for i in nums:
            arr[i] = i
        return arr.index(-1)