class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        deg = defaultdict(int)
        leng = len(edges)
        visited = set()
        for i in range(leng):
            deg[edges[i]]+=1
        ans = -1
        
        def visit(x):
            nonlocal ans
            d = 0
            mp = {}
            while x not in visited:
                mp[x] = d
                d+=1
                visited.add(x)
                if edges[x] != -1:
                    x = edges[x]
                    if x in mp:
                        ans = max(ans, d - mp[x])
        
        for i in range(leng):
            if i not in visited and deg[i] > 0 and edges[i] != -1:
                visit(i)
                
        return ans