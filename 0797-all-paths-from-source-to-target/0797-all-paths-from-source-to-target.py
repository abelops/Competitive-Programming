class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(list)
        for i in range(len(graph)):
            mp[i].extend(graph[i])
        
        fin = len(graph)
        ans = []
        def recur(n, path):
            if n == fin - 1:
                ans.append(path[:])
                return
            for i in mp[n]:
                # if i not in visited:
                path.append(i)
                recur(i, path)
                path.pop()
                
        recur(0, [0])
        
        return ans
            
        
        
        