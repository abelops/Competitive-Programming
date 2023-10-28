class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 1
        l = len(colors)
        for i in range(l):
            for j in range(i, l):
                if colors[i] != colors[j]:
                    ans = max(ans, j-i)
        return ans