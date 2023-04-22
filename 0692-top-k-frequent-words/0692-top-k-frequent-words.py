class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        count = defaultdict(list)
        for i in c:
            count[c[i]].append(i)
        ans = []
        for i in sorted(count):
            ans.extend(sorted(count[i])[::-1])
        return ans[-k:][::-1]