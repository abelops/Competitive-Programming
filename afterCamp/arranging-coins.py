class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = l + (r-l)//2
            curSum = mid*(mid+1)//2
            if curSum < n:
                l = mid + 1
            elif curSum > n:
                r = mid - 1
            else:
                return mid         
        return l-1
            