class Solution:
    def mySqrt(self, x: int) -> int:
        mp = {}
        y = 0
        while y * y < 2**32:
            if y * y == x:
                return y
            if y * y > x:
                return y-1
            mp[y] = y*y
            y+=1

        