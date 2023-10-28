class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -1 * piles[i]
        heapify(piles)
        for i in range(k):
            poped = heapq.heappop(piles)
            heappush(piles,poped//2)
        for i in range(len(piles)):
            piles[i] = -1 * piles[i]
        return sum(piles)