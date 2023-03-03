class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        flag = False
        for i in range(len(nums)):
            if nums[i] == target:
                if not flag:
                    ans[0] = i
                    if len(nums) == 1:
                        ans[1] = i
                    flag = True
                else:
                    ans[1] = i
        if ans[0] != -1 and ans[1] == -1:
            ans[1] = ans[0]
        return ans
        