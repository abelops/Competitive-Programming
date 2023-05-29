class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([amount])
        ans = float("inf")
        level = 0
        if amount == 0:
            return 0
        visited = set()
        while q:
            leng = len(q)
            for i in range(leng):
                poped = q.popleft()
                for j in coins:
                    diff = poped - j
                    if diff not in visited:
                        if diff == 0:
                            ans = min(ans, level+1)
                            # print(level, ans)
                            break
                        if diff > 0:
                            q.append(diff)
                        visited.add(diff)
            level+=1
        # print(ans)
        
        return ans if ans != float("inf") else -1