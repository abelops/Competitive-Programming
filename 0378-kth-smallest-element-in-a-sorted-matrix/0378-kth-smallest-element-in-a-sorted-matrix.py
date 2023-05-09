class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        mat = [c for b in matrix for c in b]
        heapify(mat)
        for i in range(k):
            ans = heappop(mat)
        return ans