from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return max(nums)
        ans = [max(nums[:k])]
        window = SortedList()
        for i in range(k):
            window.add(nums[i])
            
        for i in range(k, len(nums)):
            window.remove(nums[i-k])
            window.add(nums[i])
            ans.append(window[-1])
        return ans
            