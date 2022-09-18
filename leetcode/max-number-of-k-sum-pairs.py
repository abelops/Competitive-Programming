class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations, d = 0, defaultdict(int)
        for v in nums:
            res = k - v
            if d[res]:
                operations += 1
                d[res] -= 1
            else:
                d[v] += 1
        return operations