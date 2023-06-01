class Solution:
    def climbStairs(self, n: int) -> int:
        x = 1
        y = 1
        for i in range(n-2, -1, -1):
            x, y = x+y ,x
        return x
        