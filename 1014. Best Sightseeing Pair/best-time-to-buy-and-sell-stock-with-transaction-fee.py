class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        l = len(prices)
        profit = 0
        buyingCost = prices[0]
        
        for i in range(1, l):
            profit = max(profit, prices[i] - buyingCost - fee)
            buyingCost = min(buyingCost, prices[i] - profit)
            
        return profit