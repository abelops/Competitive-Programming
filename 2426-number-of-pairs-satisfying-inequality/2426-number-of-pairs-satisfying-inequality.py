from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        ans = SortedList()
        c = 0
        for i in range(n):
            c += bisect_right(ans, nums1[i] - nums2[i] + diff)
            ind = bisect_left(ans, nums1[i] - nums2[i])
            ans.add(nums1[i] - nums2[i])
        return c