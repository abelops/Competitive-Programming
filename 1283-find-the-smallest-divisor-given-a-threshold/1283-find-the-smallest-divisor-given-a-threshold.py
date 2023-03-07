class Solution:
    def getNumSum(self, nums, k):
        ans = 0
        for i in nums:
            ans+= ceil(i/k)
        return ans
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        ans = r
        while l <= r:
            mid = l + (r-l)//2
            flag = self.getNumSum(nums, mid)
            if flag <= threshold:
                r = mid - 1
                ans = min(ans, mid)
            else:
                l = mid + 1
            
        return ans