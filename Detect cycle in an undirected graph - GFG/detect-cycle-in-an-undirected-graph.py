from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		mp = defaultdict(list)
		for i in range(len(adj)):
		    for j in adj[i]:
		        if i not in mp[j]:
		            mp[i].append(j)
		            
		def dfs(cur, visited):
            if cur in visited:
                return True
            visited.add(cur)
            for i in mp[cur]:
                if dfs(i, visited):
                    return True
            return False
        
		for i in mp:
		    if dfs(i, set()):
		        return True
		return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends