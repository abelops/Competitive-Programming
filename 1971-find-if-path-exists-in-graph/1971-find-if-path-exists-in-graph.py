class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        mp = defaultdict(list)
        for i in edges:
            mp[i[0]].append(i[1])
            mp[i[1]].append(i[0])
            
        def dfs(v,visited):
            if v == destination:
                return True
            visited.add(v)
            if not mp[v]:
                return
            for i in mp[v]:
                if i not in visited:
                    found = dfs(i, visited)
                    if found:
                        return True
            return False
        visited = set()
        return dfs(source, visited)
            
            