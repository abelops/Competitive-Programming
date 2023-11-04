class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i]-curMin)
            curMin = min(curMin, prices[i])
        return maxProfit