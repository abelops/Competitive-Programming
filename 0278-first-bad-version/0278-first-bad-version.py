# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        lastBad = 1
        while low <= high:
            mid = (low + high) // 2
            isBad = isBadVersion(mid)
            if isBad:
                high = mid - 1
                lastBad = mid
            else:
                low = mid + 1
        return lastBad