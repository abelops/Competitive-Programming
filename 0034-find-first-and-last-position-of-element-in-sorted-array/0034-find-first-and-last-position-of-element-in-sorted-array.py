class Solution:
    def binSearch(self, ans, flag, nums, target):
        l = 0
        r = len(nums) -1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                if flag:
                    ans[0] = mid
                    r = mid - 1
                else:
                    ans[1] = mid
                    l = mid + 1
        return ans
            
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        call1 = self.binSearch(ans,True, nums, target)
        if call1[0] == -1:
            return ans
        ans = self.binSearch(call1,False, nums, target)
        return ans
            