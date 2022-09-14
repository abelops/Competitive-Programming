class Solution:
    def cond(x):
        return int(x)
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted(nums,key=Solution.cond,reverse=True)
        print(nums)
        return nums[k-1]