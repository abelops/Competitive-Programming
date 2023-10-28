class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors = [0] * len(graph)
        ans = []
        def dfs(i):
            if colors[i] == 1:
                return False
            if colors[i] == 2:
                return True
            colors[i] = 1
            for elem in graph[i]:
                if not dfs(elem):
                    return False
            colors[i] = 2
            ans.append(i)
            return True
            
        for i in range(len(graph)):
            if colors[i] == 0:
                dfs(i)
        return sorted(ans)
            