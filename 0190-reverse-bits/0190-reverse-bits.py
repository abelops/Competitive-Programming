class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        l = n.bit_length()
        i = l
        while l:
            ans = ans << 1
            ans += n & 1
            # ans = ans << 1
            n = n >> 1
            l-=1
        for i in range(32-i):
            ans *= 2
        return ans
            