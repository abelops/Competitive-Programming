class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        ans = sorted([(c[key], key) for key in c])[::-1]
        t = []
        for i in range(k):
            t.append(ans[i][1])
        # print(ans)
        return t
            