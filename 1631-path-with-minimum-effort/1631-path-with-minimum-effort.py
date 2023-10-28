class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r, c = len(heights), len(heights[0])
        ds = [(0,1), (1,0), (-1,0), (0, -1)]
        def inBound(x,y):
            return 0 <= x < r and 0 <= y < c
            
        dist = { x: float("inf") for x in range(r*c)}
        dist[0] = 0
        
        queue = [(0, 0)]
        visited = set()
        
        while queue:
            d, node = heappop(queue)
            if node == r*c-1:
                return d
            x = node//c
            y = node%c
            
            if node in visited:
                continue
            visited.add(node)
            
            for a, b in ds:
                dx = x + a
                dy = y + b
                if inBound(dx, dy):
                    distance = max(dist[node], abs(heights[x][y] - heights[dx][dy]))
                    if dist[dx*c +dy] > distance:
                        dist[dx*c +dy] = distance
                        heappush(queue, (distance, dx*c + dy))
                        
                
            