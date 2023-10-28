class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        mp = defaultdict(list)
        for i,node in enumerate(equations):
            start, end = node
            mp[start].append((values[i], end))
            mp[end].append((1/values[i], start))
        
        
        def dfs(start, end):
            if start not in mp or end not in mp:
                return -1
            q = deque([(1,start)])
            visited = set()
            visited.add(start)
            while q:
                w, poped = q.popleft()
                if poped == end:
                    return w

                for val, node in mp[poped]:
                    if node not in visited:
                        visited.add(node)
                        q.append((w*val, node))

            return -1
        return [dfs(src,target) for src,target in queries]