class Solution:
    def racecar(self, target: int) -> int:
        visited = set((0,1))
        q = deque([(0,1)])
        level = 0
        while q:
            l = len(q)
            for _ in range(l):
                a, b = q.popleft()
                if a == target:
                    return level
                n1 = (a+b, b*2)
                n2 = (a, -1) if b > 0 else (a,1)
                if n1 not in visited :
                    q.append(n1)
                    visited.add(n1)
                if n2 not in visited:
                    q.append(n2)
                    visited.add(n2)
            level+=1
        return ans
        
