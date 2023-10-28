class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        def bfs(src, dest):
            q = deque([(src, [src])])
            visited = set()
            while q:
                node, path = q.popleft()
                if node == dest:
                    return path
                visited. add (node)
                for nei in graph [node]:
                    if nei not in visited:
                        q.append((nei, path + [nei]))
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        freq = defaultdict(int) 
        for src, dest in trips:
            path = bfs(src, dest)
            for node in path:
                freq[node] += 1
        
        @cache
        def dp(node, parent, shouldHalf):
            if shouldHalf:
                cost = freq[node] * price[node] //2
            else:
                cost = freq[node] * price[node]
            
            for nei in graph[node]:
                if nei != parent:
                    if shouldHalf:
                        nei_cost = dp(nei, node, False)
                    else:
                        nei_cost = min(dp(nei, node, False), dp(nei, node, True))
                    cost += nei_cost
            return cost

        cost = float("inf")
        for i in range(n):
            cost = min(cost, dp(i, None, False), dp(i, None, True))
        return cost
    