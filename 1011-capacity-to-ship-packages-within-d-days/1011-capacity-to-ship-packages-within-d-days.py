class Solution:
    def getMinShip(self, shipment, k):
        ans = 0
        c = 0
        for i in range(len(shipment)):
            if ans + shipment[i] > k:
                c += 1
                ans = shipment[i]
            else:
                ans += shipment[i]
        if ans > 0:
            c += 1
        return c
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = 1
        r = sum(weights)
        ans = r
        while l <= r:
            mid = l + (r-l)//2
            if mid < max(weights):
                l = mid +1
                continue 
            if self.getMinShip(weights, mid) <= days:
                r = mid - 1
                ans = min(ans, mid)
            else:
                l = mid + 1
        return ans
    