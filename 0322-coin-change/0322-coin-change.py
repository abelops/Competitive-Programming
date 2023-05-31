class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [-1] * (amount + 1) 
        arr[0] = 0
        for i in range(1,amount+1):
            minn = float("inf")
            for j in coins:
                diff = i - j
                if diff >= 0:
                    # if arr[diff] != -1:
                    minn = min(minn, arr[diff]+1)
            arr[i] = minn
        return arr[-1] if arr[-1] != float("inf") else -1
                        
            