class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1), len(s2)
        memo = {}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == l1:
                return sum([ord(s2[ind]) for ind in range(j, l2)])
            if j == l2:
                return sum([ord(s1[ind]) for ind in range(i, l1)])
            ans = float('inf')
            if s1[i] != s2[j]:
                ans = min(dp(i+1, j) + ord(s1[i]), ans)
                ans = min(dp(i, j+1) + ord(s2[j]), ans)
            else:
                ans = min(dp(i+1, j+1), ans)
            memo[(i,j)] = ans
            return ans
        return dp(0,0)
            