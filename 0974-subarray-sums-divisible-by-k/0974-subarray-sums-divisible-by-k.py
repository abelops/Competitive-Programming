class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        csum, ans = 0, 0
        D = [0] * k
        D[0] = 1
        for i in nums:
            csum = (csum + i) % k
            ans += D[csum]
            D[csum] += 1
        return ans
            
            