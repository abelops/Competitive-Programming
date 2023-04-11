class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        noStart = set([x[1] for x in edges])
        return list(set([x for x in range(n)]).difference(noStart))
            