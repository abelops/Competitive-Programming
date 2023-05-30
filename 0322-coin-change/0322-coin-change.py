class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        if len(coins) == 1 and amount % coins[0] != 0:
            return -1
        def backtrack(cur):
            if cur == 0:
                return 0
            if cur in memo:
                return memo[cur]
            minn = float("inf")
            for j in coins:
                if cur - j >= 0:
                    temp = backtrack(cur-j)
                    minn = min(minn, temp)
            memo[cur] = minn + 1
            return minn + 1
        ans = backtrack(amount)
        return ans if ans != float("inf") else -1 
            
            