class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = {}
        ans = []
        if n == 0:
            return 0
        def recur(x):
            nonlocal ans
            if x < 2:
                ans.append(x)
                memo[x] = x
                return x
            if x % 2 == 0 and x//2 in memo:
                memo[x] = memo[x//2]
                ans.append(memo[x])
                return memo[x]
            elif (x - 1)//2 in memo:
                memo[x] = memo[(x-1)//2] + memo[((x-1)//2) + 1]
                ans.append(memo[x])
                return memo[x]
            recur(x-1)
            recur(x-2)
        recur(n+2)
        return max(memo.values())