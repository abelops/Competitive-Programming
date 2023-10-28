class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        c=0
        if(len(nums)%2!=0):
            c = 1
        for i in range(0,len(nums)-c,2):
            tem = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = tem
        return nums
            