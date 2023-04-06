class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = None
        backUp = n
        while n:
            opp = n & 1
            if prev == opp:
                return False
            n >>= 1
            prev = opp
        return True