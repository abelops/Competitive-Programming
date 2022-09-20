class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ns = Counter(nums)
        val = sorted(ns.items(), key=lambda item: item[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(list(val)[i][0])
        return ans