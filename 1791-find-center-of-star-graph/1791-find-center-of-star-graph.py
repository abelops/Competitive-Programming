class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ans = set(edges[0])
        for i in edges:
            ans &= set(i)
        return list(ans)[0]