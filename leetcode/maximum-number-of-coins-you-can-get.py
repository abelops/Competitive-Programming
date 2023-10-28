class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        stack1 = piles
        stack2 = piles[0:int(len(piles)/3)]
        l = len(stack2)
        su = 0
        for i in range(l):
            stack2.pop()
            stack1.pop()
            su+=stack1.pop()
            
        return su
            