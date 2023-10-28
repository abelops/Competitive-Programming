class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (start, end) in enumerate(edges):
            graph[start].append((end, succProb[i]))
            graph[end].append((start, succProb[i]))
        
        dist = {x:float("-inf") for x in range(n)}
        dist[start_node] = 1
        queue = [(-1, start_node)]
        visited = set()
        
        while queue:
            d, node = heapq.heappop(queue)
            d*=-1
            if node in visited:
                 continue
            visited.add(node)

            for neighbor, weight in graph[node]:
                distance = d * weight
                if distance > dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(queue, (-distance, neighbor))
        
        return dist[end_node] if dist[end_node]!= float("-inf") else 0
        
        
        