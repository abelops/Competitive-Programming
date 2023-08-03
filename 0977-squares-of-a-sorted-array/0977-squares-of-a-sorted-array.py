class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        ans = []
        while l <= r:
            num1 = nums[l] ** 2
            num2 = nums[r] ** 2
            if num1 > num2:
                ans.append(num1)
                l+=1
            else:
                ans.append(num2)
                r-=1
        return ans[::-1]