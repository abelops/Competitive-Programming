class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        heapq.heapify(stones)
        while len(stones) > 1:
            n1 = abs(heapq.heappop(stones))
            n2 = abs(heapq.heappop(stones))
            if n1 != n2 or not stones:
                heapq.heappush(stones,-1*(n1- n2))
        return stones[0] * -1
        
        