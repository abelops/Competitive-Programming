class NumArray:

    def __init__(self, nums: List[int]):
        self.pref = [0,nums[0]]
        for i in range(1,len(nums)):
            self.pref.append(self.pref[-1]+nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.pref[right+1]-self.pref[left]
            


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)