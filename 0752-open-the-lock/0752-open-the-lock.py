class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends or target in deadends:
            return -1
        q = deque([[0,0,0,0]])
        visited = set((0,0,0,0))
        def gen(arr):
            ans = []
            for i in range(4):
                plus = arr[i]+1
                if plus > 9:
                    plus = 0
                minus = arr[i]-1
                if minus < 0:
                    minus = 9
                temp = arr[:]
                temp[i] = plus
                ans.append(temp)
                temp = arr[:]
                temp[i]=minus
                ans.append(temp)
            return ans
        level = 0         
        while q:
            l = len(q)
            for i in range(l):
                poped = q.popleft()
                ch = "".join(map(str,poped))
                if ch == target:
                    return level
                neigbour = gen(poped)
                for j in neigbour:
                    if tuple(j) not in visited and "".join(map(str,j)) not in deadends:
                        q.append(j)
                        visited.add(tuple(j))
            level += 1
        return -1
                        
                