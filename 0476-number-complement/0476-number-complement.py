class Solution:
    def findComplement(self, num: int) -> int:
        bitLen = num.bit_length()
        return num ^ ((1 << bitLen) -1)