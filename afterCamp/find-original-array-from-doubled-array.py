class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        l = len(changed)
        if l % 2 != 0:
            return []
        changed.sort()
        visited = defaultdict(int)
        ans = []
        for i in changed:
            visited[i] += 1
        for i in range(l):
            n = changed[i]
            if visited[n] <= 0:
                continue
            if visited[n*2] <= 0:
                return []
            ans.append(n)
            visited[n*2]-=1
            visited[n]-=1
        return ans
                
                
        
        
        