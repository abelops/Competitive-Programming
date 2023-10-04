class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, d in times:
            graph[start-1].append((end-1, d))
        distance = { x: float('inf') for x in range(n)}
        distance[k-1] = 0
        visited = set()
        queue = [[0, k-1]]
        while queue:
            cur_dist, node = heapq.heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            
            for neighbor, weight in graph[node]:
                dist = cur_dist + weight
                if dist < distance[neighbor]:
                    distance[neighbor] = dist
                    heapq.heappush(queue, (dist, neighbor))
        ans = max(distance.values())
        
        return  ans if ans != float('inf') else -1 
            

                
        