class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city, visited):
            visited.add(city)
            
            for i in range(len(isConnected)):
                if isConnected[city][i] and i!=city and i not in visited:
                    dfs(i, visited)
        visited = set()
        ans = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i, visited)
                ans+=1
        return ans
            
            
            