class Solution:
    def getPileSum(self, piles, k):
        ans = 0
        for i in piles:
            ans+= ceil(i/k)
        return ans
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # lis = [ x for x in range(1,max(piles)+1)]
        l = 1
        r = max(piles)
        ans = r
        while l <= r:
            mid = l + (r-l)//2
            flag = self.getPileSum(piles, mid)
            if flag <= h:
                r = mid - 1
                ans = min(ans, mid)
            else:
                l = mid + 1
            
        return ans