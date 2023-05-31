class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        seq = [0,1,1]
        for i in range(3, n+1):
            tot = seq[-1] + seq[-2] + seq[-3]
            seq.append(tot)
        return seq[-1]