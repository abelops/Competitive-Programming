class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def recur(x):
            if x == 0:
                return 0
            if x < 3:
                return 1
            if x in memo:
                return memo[x]
            a = recur(x-1)
            y = recur(x-2)
            z = recur(x-3)
            memo[x] = a + y + z
            return a + y + z 
        return recur(n)