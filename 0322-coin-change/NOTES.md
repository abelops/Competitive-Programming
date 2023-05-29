class Solution:
def coinChange(self, coins: List[int], amount: int) -> int:
memo = {}
def backtrack(cur, i):
if cur == 0:
return i
minn = float("inf")
# if cur in memo:
#     return memo[cur] + i
for j in coins:
if cur - j >= 0:
temp = backtrack(cur-j, i+1)
if temp != -1:
minn = min(minn, temp)
if minn != float("inf"):
memo[cur] = minn
return minn if minn != float("inf") else -1
ans = backtrack(amount, 0)
print(memo)
return ans