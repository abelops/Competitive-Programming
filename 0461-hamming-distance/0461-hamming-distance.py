class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        ans = 0
        while xor:
            if xor & 1:
                ans+=1
            xor >>= 1
        return ans