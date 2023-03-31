class Solution:
    def findComplement(self, num: int) -> int:
        bitLen = num.bit_length()
        one = (1 << bitLen) -1
        return num ^ one