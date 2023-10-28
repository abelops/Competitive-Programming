class Solution:
    def countOrders(self, n: int) -> int:
        ans = 1
        for i in range(n*2, 0, -2):
            ans *= i * (i -1)//2
        return ans % (10**9 +7)
        