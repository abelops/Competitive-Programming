class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l = len(piles)//3
        su = 0
        for i in range(l):
            piles.pop()
            su+=piles.pop()
        return su
            