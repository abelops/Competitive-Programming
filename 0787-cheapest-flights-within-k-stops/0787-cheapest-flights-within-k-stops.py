class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
            
        dist = {node: float("inf") for node in range(n)}
        dist[src] = 0
        
        q = [(0, 0, src)]
        ans = float("inf")
        while q:
            cts, d, node = heappop(q)
            if cts > k:
                continue
            for neighbor, w in graph[node]:
                newWeight = d + w
                newCount = cts + 1
                if neighbor == dst:
                    # print('here', dist, newCount,newWeight)
                    if newCount-1 <= k:
                        ans = min(ans, dist[neighbor], newWeight)
                # print(dist, neighbor)
                if newWeight < dist[neighbor]:
                    dist[neighbor] = newWeight
                    heappush(q, (newCount, newWeight, neighbor))
        # print(dist)
        return ans if ans != float("inf") else -1
        
        