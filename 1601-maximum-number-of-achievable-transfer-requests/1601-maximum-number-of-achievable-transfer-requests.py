class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # ans = []
        c = 0
        memo = {}
        def helper(arr):
            nonlocal memo
            if tuple(arr) not in memo:
                leave = {}
                join = {}
                for i in arr:
                    leave[i[0]] = leave.get(i[0], 0) + 1
                    join[i[1]] = join.get(i[1], 0) + 1
                memo[tuple(arr)] = [leave, join]
            else:
                join = memo[tuple(arr)][0]
                leave = memo[tuple(arr)][1]
                
            return join == leave
        
        def comb(start, cur):
            nonlocal c
            if cur:
                if helper(cur[:]):
                    c = max(c, len(cur))
            for i in range(start, len(requests)):
                cur.append(tuple(requests[i]))
                comb(i+1, cur)
                cur.pop()
        comb(0, [])
        return c