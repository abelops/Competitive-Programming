class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = len(citations)-1
        n = len(citations)
        while l <= r:
            mid = l + (r-l)//2
            if n - mid > citations[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return n - l