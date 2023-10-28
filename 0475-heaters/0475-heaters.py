class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0
        hi = 0
        for house in houses:
            near = bisect.bisect(heaters,house)
            if near >= len(heaters):
                ans = max(ans,abs(heaters[near-1]-house))
            else:
                ans = max(ans,min(abs(heaters[near-1]-house), abs(heaters[near]-house)))
        return ans